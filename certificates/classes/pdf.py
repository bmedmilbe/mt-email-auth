# # class PDF():
# #     pass

from decimal import Decimal
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.files import File
import uuid
from django.conf import settings
#  require_once("files/dompdf/autoload.inc.php");
#  use Dompdf\Dompdf;
from django.core.files.storage import default_storage
from certificates.classes.string_helper import StringHelper
from certificates.models import Certificate, CertificateDate, CertificateTitle, CertificateTypes, Ifen, Person

from datetime import date, timedelta
import boto3


from pprint import pprint


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('invoice.html')
#         context = { "invoice_id": 123, "customer_name": "John Cooper", "amount": 1399.99, "today": "Today", }
#         html = template.render(context)
#         pdf = render_to_pdf('invoice.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#                 response['Content-Disposition'] = content
#                 return response

#         return HttpResponse("Not found")

# from storages.backends.s3boto3 import S3Boto3Storage


class PDF():
    def __init__(self, text, type1: CertificateTypes, type2: CertificateTitle, gerado: Certificate, form, bi: Person):
        self.pdf_root = ""
        self.pdf_name = ""
        self.pdf_number = ""

        self.text = text
        self.type1 = type1
        self.type2 = type2
        self.certificate = gerado
        self.data = form
        self.bi = bi
        self.presidente = "ANAHORY DIAS ABÍLIO DO ESPÍRITO"
        self.distrito = "MÉ-ZÓCHI"
        self.date = StringHelper.ext_data(StringHelper, gerado.date_issue)

        self.footer = StringHelper.data(StringHelper, gerado.date_issue)

        self.final_text = self.textoFinal(
            self.type1, self.data.get('last_date'))

        value = type2.type_price
        if type2.id == 8 and self.bi.birth_address.id in [3, 4, 7, 8, 9, 12, 13, 14, 15]:
            self.conta_details = self.conta(
                type1, type2, gerado.number, 1847.5, True)

        elif type2.id == 8:
            self.conta_details = self.conta(
                type1, type2, gerado.number, 2460, True)

        elif type2.id == 25:
            self.conta_details = self.conta(
                type1, type2, gerado.number, self.data['change'].price)
        elif type2.id == 29:
            if not self.data['metros']:  # metros none
                value = 250 * self.data['dates'].count()
            else:
                if self.data['metros'] >= 4:
                    value = 175 * self.data['dates'].count()
                else:
                    value = 175 * self.data['dates'].count() + (
                        int(self.data['metros']) - 4) * 50 * self.data['dates'].count()

                value = (value) + 10

            self.conta_details = self.conta(type1, type2, gerado.number, value)
        elif type2.id == 32:

            value = type2.type_price + 10

            self.conta_details = self.conta(type1, type2, gerado.number, value)
        else:
            self.conta_details = self.conta(type1, type2, gerado.number, value)

    def render_pdf(self):
        ifen = Ifen.objects.get(name="data")
        dash = ifen.size * " -"

        self.date = f"- - - Câmara Distrital de {self.bi.address.street.town.county.name}, na Cidade da {self.bi.address.street.town.name}, aos {self.date}."

        # size = Ifen.objects.filter(name='DATA').first().size

        

        self.date = f"{self.date}{dash[len(self.date):]}"

        ifen = Ifen.objects.get(name="texto")
        dash = ifen.size * " -"
        self.text = f"- - - {self.text}{dash[len(self.text):]}"

        # self.footer = StringHelper.data(StringHelper,gerado.date_issue)
        # Col
        # Câmara Distrital de {{distrito}}, na Cidade da {{town}}, aos
    #   {{date}}

        template = get_template("certificates/certificate_off.html")
        context = {}
        context_dict = {
            'body': self.text,
            'presidente': f"{self.presidente}",
            # 'distrito':f"{self.distrito}",
            'distrito': f"{self.bi.address.street.town.county.name.upper()}",
            'town': f"{self.bi.address.street.town.name}",
            # 'presidente':f"{self.presidente}, presidente da camarâ distrtrital de {self.distrito}",
            'certificate': self.certificate,
            'type1': self.type1,
            'type2': self.type2,
            'final_text': self.final_text,
            'date': self.date,
            'data': self.data,
            'prices': self.conta_details,
            'bi': self.bi,
            'logo': 'https://bm-edmilbe-bucket.s3.eu-north-1.amazonaws.com/camaramz/extras/stp.41e0f117.png'
        }
        # pprint(context_dict['prices'])
        html = template.render(context_dict)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        # pprint(result.getvalue())

        # file_name = uuid.uuid4()
        file_path = self.certificate.number
        file_path = f"/certificates/{self.type2.id}-{self.type1.slug}-de-{self.type2.slug}/{file_path}.pdf"
        folder_online = f"{self.type2.id}-{self.type1.slug}-de-{self.type2.slug}/{self.certificate.number}.pdf"
        try:
            path = str(settings.MEDIA_ROOT) + \
                f"{file_path}"
            with open(path, 'wb+') as output:
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), output)
                # pprint(path)
                certificate = Certificate.objects.get(id=self.certificate.id)
                certificate.file.save(f'{folder_online}', File(output))
                file_path = certificate.file.url
                print("file_nama: ", file_path)

        except Exception as e:
            print("error", e)

        if pdf.err:
            return '', False

        return file_path, True

    def conta(self, type1: CertificateTypes, type2: CertificateTitle, atestado_number, autoV=0, cplp=False):

        # pprint("type1:")
        # pprint(type1)
        # pprint("type2:")
        # pprint(type2)
        value = type2.type_price

        Total = 0
        Rasa = 10
        if type2.id == 33:
            value = type2.type_price
            Total = value
            value = value

        elif type2.id in [25, 29] or type2.id == 8 and cplp == True:
            Rasa = 100
            value = autoV
            Total = Total + Rasa
        elif type2.id == 32:
            value = autoV
            Total = Rasa + 20
        else:
            Rasa = 5
            Total = Total + Rasa

        Selo = 10
        Total = Total + Selo
        Imposto = (value - (10)) * Decimal(0.1)
        Total = Total + Imposto
        Emolumento = (value - 10) - Rasa - Imposto
        Total = Total + Emolumento

        Zero = Emolumento + Rasa
        Rasa = 0 if Zero == 0 else Rasa
        Emolumento = 0 if Zero == 0 else Emolumento
        # pprint(Emolumento)
        Emolumento = round(Emolumento, 2)
        Rasa = round(Rasa, 2)
        Selo = round(Selo, 2)
        Imposto = round(Imposto, 2)

        Total = round(Total, 2)

        return {
            'total': Total,
            'rasa': Rasa,
            'selo': Selo,
            'emolumento': Emolumento,
            'imposto': Imposto,
            'total_extenso': StringHelper.NumeroEmExtenso(Total)
        }

    def setTracoCenter(self, ct, string):

        c = int((ct - len(string)) / 2)

        newString = ""

        for i in range(0, c+1):
            newString = f"{newString}-"

        newString = f"{newString}{string}"

    def setTracoData():
        return f"{Ifen.objects.get(name='DATA')}"

    def setTracoValidade():
        return f"{Ifen.objects.get(name='VALIDADE')}"

    def setTracoLast(self, ct, string):
        c = int((ct - len(string)))
        newString = f"------{string}"
        for i in range(0, c):
            newString = f"{newString}-"

        return newString

    def textoFinal(self, type1: CertificateTypes, expire_date=None):
        text_ifen = 109 * " -"
        text = f"""
        - - - Por ser verdade e ter sido requerido, mandou passar {type1.gender} presente {type1.name}, que assina, sendo a sua assinatura autenticada com o carimbo em uso nesta Câmara."""
        text = text + text_ifen[len(text):]

        if type1.id in [3, 4, 7]:
            text = ""
        elif type1.id == 6:
            startdate = date.today()
            enddate = startdate + timedelta(days=365)  # five years ago
            validade = StringHelper.ext_data(StringHelper, enddate)
            text = f"""{text}
            - - - Válida até {validade}"""
        elif type1.id == 8:
            # pprint("Aqui")
            # pprint(StringHelper.ext_data(StringHelper,expire_date))
            rest = 5 * " -"
            size = 62 * " -"
            temp_text = f"- - - Válida até {StringHelper.ext_data(StringHelper,expire_date)}."
            text = f"""{text}
            {temp_text}{size[len(temp_text):]}
            - - - Às autoridades e mais a quem o conhecimento desta competir assim o tenham entendido.{rest[1:]}"""

        return text

    def data(timestamp_date):
        startdate = date.today()
        data = StringHelper.DataEmExtenso(
            startdate.day, startdate.month, startdate.year)
        string = f"------Câmara Distrital de Mé-Zóchi, na Cidade da Trindade, aos {data}.{self.setTracoData()}"

        return string
