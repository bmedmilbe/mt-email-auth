from certificates.models import CertificateSinglePerson
from .pdf import PDF
from .string_helper import StringHelper
from certificates.classes.interfaces.document import Document
from pprint import pprint
from .document_data import DocumentData

class AutoEnterro(Document):
    def __init__(self,data: DocumentData):
        self.data = data
        self.text = ""

    def create_text(self):
        data = self.data

        tempo = ""

        #name, sexo, coval (generate), cemiterio, seputado(get old), pedi(get old)
        # this.text = "Autorizo o enterro do(a) ". toBold($this->getForm()->getCovalData()->getCovalSepultado())
        #     ." no coval número " . $this->getForm()->getCovalData()->getCovalNumber(). ", antigo " . $this->getForm()->getCovalData()->getCovalLastname()
        #     .", do Cemitério de " .
        #     $this->getForm()->getCovalData()->getCovalCemiterio()->getDistritoName() . ", falecido(a) em ".
        #     $this->getForm()->getCovalData()->getCovalFalecimento()->getExtData()
        #     ." e Sepultado(a) " . $this->getForm()->getCovalData()->getCovalLastused()->getExtData()
        # . ", ao pedido " . " d".$this->getBi1()->getBiOa() .  " senhor" .$this->getBi1()->getBiOa2() . " " .
        #     StringHelper::getTextBi($this->getBi1(), $this->getBi2(),$this->getType2()->getTypeId(), $this->getForm())
        #     . "residente em " . $this->getForm()->getLocalidade()->getLocalidadeFull() .
        #     ".";
        single_person = CertificateSinglePerson.objects.filter(type_id=data.type2.id).first()
        single_person_text = f"d{StringHelper.oa(StringHelper,single_person.gender)} {StringHelper.toBold(single_person.name)},"




        self.text = f"Autorizo o enterro {single_person_text} no coval número {data.data['coval'].number}, antigo {data.data['last_coval'].number}, do Cemitério de {data.data['cemiterio'].name}, falecid{StringHelper.oa(StringHelper,single_person.gender)} em {StringHelper.ext_data(StringHelper,data.data['died_date'])} e Sepultad{StringHelper.oa(StringHelper,single_person.gender)} em {StringHelper.ext_data(StringHelper,data.data['entero_date'])}, ao pedido d{StringHelper.oa(StringHelper,data.bi1.gender)}{StringHelper.text_bi(StringHelper, data.type2,data.bi1,data.bi2,data.data)} residente em {StringHelper.house_address(StringHelper, data.bi1.address)}."
        

        pdf_object = PDF(self.text,self.data.type,self.data.type2, data.certificate, self.data.data,self.data.bi1)
        file_name, status = pdf_object.render_pdf()
        return self.text, file_name, status

        # return new PDF($this->text,$this->getType(),$this->getType2(), $this->getGerados(), $this->getForm());
#    `    `

#     /**
#      * @return mixed
#      */
#     public function getText()
#     {
#         return $this->text;
#     }



#     function store()
#     {
#         $this->storeInDB($this);

#         // TODO: Implement create() method.
#         dnd($this);

#     }

#     function read()
#     {
#         // TODO: Implement read() method.
#     }

#     function aproveFirst()
#     {
#         // TODO: Implement aproveFirst() method.
#     }

#     function aproveSecond()
#     {
#         // TODO: Implement aproveSecond() method.
#     }

# }