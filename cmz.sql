

COPY "public"."cmz_imagestour" ("id", "image", "tour_id") FROM stdin;
2	camaramz/tour/images/Roça_Monte_Café_-_São_Tomé_e_Príncipe_Foto_de_Avlis_Rotieh.jpg	2
3	camaramz/tour/images/Captura_de_ecrã_2020-03-14_às_14.22.00.png	2
4	camaramz/tour/images/roc3a7a-monte-cafc3a9-distrito-de-mc3a9-zoxi-ilha-de-sc3a3o-tomc3a9.jpg	2
5	camaramz/tour/images/Roca-Bombaim.Sao-Tome.www_.saotomechoice.com_.jpg	3
6	camaramz/tour/images/bombaim02.jpg	3
7	camaramz/tour/images/sao-tome-2022-0159-1.jpg	4
8	camaramz/tour/images/download.jpeg	4
9	camaramz/tour/images/pico-de-sao-tome.jpg	4
\.


--
-- Data for Name: cmz_information; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_information" ("id", "information", "question", "service_id") FROM stdin;
2	Cada atestado tem uma finalidade diferente, veja abaixo todos os tipos de atestados que emitimos:\r\n- Abertura de Conta Bancária\r\n- Agregado Familiar\r\n- Assistência Judicial\r\n- Bolsa de Estudo\r\n- Bolsa Interna\r\n- Candidatura à Transporte Público\r\n- Cargo Público\r\n- Casamento\r\n- Convenientes\r\n- Emprego\r\n- Escolares\r\n- Fixação de Residência\r\n- Nacionalidade Santomense\r\n- Obtenção de Visto\r\n- Percepção da Pensão de Aposentação\r\n- Percepção da Pensão de Reforma\r\n- Percepção da Pensão de Sobrevivência por Morte\r\n- Profissionais\r\n- Prova de Vida\r\n- Residência\r\n- Subsídio de Transporte\r\n- Transferência de mesada monetária\r\n- Viagem	Que atestados emitimos?	2
4	Qualquer residente do Distrito de Mé-Zóch que seja maior de idade pode requerer um atestado de acordo ao sua necessidade.	Quem pode requerer um atestado?	2
5	O requesito básico necessário para emissão de atestado é o bilhete de identidade válido e ser residente no Distrito de Mé-Zóchi.	Quais são os documentos necessários para requerer um atestados?	2
3	Maioria dos atestados custam 140.00 STN, com excepção desses abaixos que têm outros preços:\r\n- Assistência Judicial: 210.00 STN\r\n- Fixação de Residência: 2460.00 STN\r\n- Nacionalidade Santomense: 510.00 STN\r\n- Percepção da Pensão de Aposentação: 10.00 STN\r\n- Percepção da Pensão de Reforma: 10.00 STN\r\n- Profissionais: 100.00 STN\r\n- Prova de Vida: 10.00 STN\r\n- Transferência de Mesada Monetária: 100.00 STN	Qual é o custo dos atestados?	2
6	A lista abaixo indicada contem todos os tipos de licenças e autorizações que nós emitimos:\r\n- Autorização de Construção\r\n- Autorização de Enterro\r\n- Autorização modificação, construção da sua barraca em alvenaria\r\n- Autorização para Modificar o Coval\r\n- Certificado de Compra de Coval\r\n- Licença para BufettLicenças para Baile\r\n- Licenças Para Barraca\r\n- Licenças Para Transladação	Que autorização ou licença emitimos?	1
7	As licenças têm preços distintos consoante as circunstáncias no entanto a lista abaixo ilustra os preços base de diferentes licenças:\r\n- Autorização de Construção: 1010.00 STN\r\n- Autorização de Enterro: 500.00 STN\r\n- Autorização modificação, construção da sua barraca em alvenaria: 1010.00 STN\r\n- Autorização para Modificar o Coval: 300.00 STN\r\n- Certificado de Compra de Coval: 25010.00 STN\r\n- Licença para BufettLicenças para Baile:\r\n- Licenças Para Barraca: 510.00 STN\r\n- Licenças Para Transladação: 500.00 STN	Quanto custa uma licença?	1
8	O requesito básico necessário para emissão de licença é o bilhete de identidade válido e ter outros documentos relacinados com a propriedade em causa.	Quais são os documentos necessários para requerer uma licença?	1
9	Qualquer pessoa maior de 18 anos e com os documentos válidos pode requerer uma licença.	Quem pode requerer um atestado?	1
10	Os beneficiários devem pagar 50.00 STN por mês para continuar a ter um caixote de lixo que a Câmara Distrital de Mé-Zóchi, irá recolher todos os finais de semana.	Qual é o custo?	3
11	Ser residente no distrito de Mé-Zóchi e ter um documento de identificação válido.	Quais são os requisitos para obter um caixote?	3
\.


--
-- Data for Name: cmz_messages; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_messages" ("id", "name", "text", "sent", "date", "subject_id", "whatsapp") FROM stdin;
\.


--
-- Data for Name: cmz_post; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_post" ("id", "title", "slug", "picture", "text_file", "active", "date", "user_id") FROM stdin;
2	Assembleia Distrital de Mé-Zóchi	assembleia-distrital-de-me-zochi	camaramz/posts/images/368565424_862228891940792_673255917237462719_n.jpg	camaramz/posts/documents/A_Assembleia_Distrital_de_Mé.docx	t	2023-08-17 10:58:06.492265+00	8
4	Fábrica de Farinha Mandioca em San Nguembú	fabrica-de-farinha-mandioca-em-san-nguembu	camaramz/posts/images/Untitled_design_10.png	camaramz/posts/documents/inbound7562131044315581114.docx	t	2023-11-27 10:07:29.763463+00	8
3	Apresentação do Projecto TRI/STP	apresentacao-do-projecto-tristp	camaramz/posts/images/Untitled_design_11.png	camaramz/posts/documents/inbound630360240809010867.docx	t	2023-11-15 10:10:37.787214+00	8
6	Reforço do Abastecimento Hídrico	reforco-do-abastecimento-hidrico	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.44.45.jpeg	camaramz/posts/documents/Reforço.docx	t	2024-01-15 14:29:25.891776+00	8
5	Balanço de Produtividade e Desempenho	balanco-de-produtividade-e-desempenho	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.19.41.jpeg	camaramz/posts/documents/Balanço.docx	t	2024-01-15 14:24:24.533506+00	8
7	Homenagem á Concidadão Mé-Zóchiano Azoumé Pinto	homenagem-a-concidadao-me-zochiano-azoume-pinto	camaramz/posts/images/421814926_888664576593552_7089521223899008386_n.jpg	camaramz/posts/documents/Câmara_Distrital_de_Mé.docx	t	2024-01-22 12:36:21.828791+00	8
8	3 de Fevereiro 2024	3-de-fevereiro-2024	camaramz/posts/images/Inserir_um_pouquinho_de_texto.png	camaramz/posts/documents/MASSACRE.docx	t	2024-02-05 10:37:28.989047+00	8
9	Foto Galeria 3 de Fevereiro- Resumo das Actividades	foto-galeria-3-de-fevereiro-resumo-das-actividades	camaramz/posts/images/2.jpg	camaramz/posts/documents/MASSACRE.docx	t	2024-02-05 10:47:46.365484+00	8
10	Iniciativa dos 5 Irmãos	iniciativa-dos-5-irmaos	camaramz/posts/images/WhatsApp_Image_2024-02-13_at_22.15.46.jpeg	camaramz/posts/documents/Iniciativa_dos_5_Irmãos.docx	t	2024-02-14 10:06:50.957464+00	8
11	Visita de Fiscalização e Levantamento	visita-de-fiscalizacao-e-levantamento	camaramz/posts/images/WhatsApp_Image_2024-02-25_at_23.37.25.jpeg	camaramz/posts/documents/Visita_de_Fiscalização_e_Levantamento.docx	t	2024-02-29 10:47:24.660396+00	8
12	AGI GÓCI	agi-goci	camaramz/posts/images/WhatsApp_Image_2024-02-25_at_23.38.16.jpeg	camaramz/posts/documents/Visita_de_Fiscalização_e_Levantamento.docx	t	2024-03-01 10:23:08.535995+00	8
\.


--
-- Data for Name: cmz_postdocument; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_postdocument" ("id", "document", "post_id") FROM stdin;
\.


--
-- Data for Name: cmz_postfile; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_postfile" ("id", "file") FROM stdin;
\.


--
-- Data for Name: cmz_postimages; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_postimages" ("id", "picture", "post_id") FROM stdin;
1	camaramz/posts/images/inbound3390652966608552373.jpg	3
2	camaramz/posts/images/inbound6952698231264542562.jpg	3
3	camaramz/posts/images/inbound2597711563573809768.jpg	3
4	camaramz/posts/images/inbound4920528555470060780.jpg	4
5	camaramz/posts/images/inbound3157586383544139926.jpg	4
6	camaramz/posts/images/inbound8217458530657527548.jpg	4
7	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.19.43.jpeg	5
8	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.19.42_1.jpeg	5
9	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.19.42.jpeg	5
10	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.44.46.jpeg	6
11	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.44.49.jpeg	6
12	camaramz/posts/images/WhatsApp_Image_2024-01-15_at_00.44.47_1.jpeg	6
13	camaramz/posts/images/421855016_888664579926885_6220399557405420842_n.jpg	7
14	camaramz/posts/images/421859696_888664659926877_3619290202195082882_n.jpg	7
15	camaramz/posts/images/421899968_888664656593544_3399797336933120455_n.jpg	7
16	camaramz/posts/images/1.jpg	9
17	camaramz/posts/images/3.jpg	9
18	camaramz/posts/images/4.jpg	9
19	camaramz/posts/images/5.jpg	9
20	camaramz/posts/images/6.jpg	9
21	camaramz/posts/images/WhatsApp_Image_2024-02-04_at_23.30.35.jpeg	9
22	camaramz/posts/images/WhatsApp_Image_2024-02-04_at_23.30.33.jpeg	9
23	camaramz/posts/images/WhatsApp_Image_2024-02-04_at_23.30.34.jpeg	9
24	camaramz/posts/images/WhatsApp_Image_2024-02-04_at_23.30.05.jpeg	9
25	camaramz/posts/images/massacre2.jpg	9
26	camaramz/posts/images/WhatsApp_Image_2024-02-13_at_22.04.01.jpeg	10
27	camaramz/posts/images/WhatsApp_Image_2024-02-13_at_22.03.45.jpeg	10
28	camaramz/posts/images/WhatsApp_Image_2024-02-13_at_22.03.55.jpeg	10
29	camaramz/posts/images/WhatsApp_Image_2024-02-13_at_22.04.06.jpeg	10
30	camaramz/posts/images/WhatsApp_Image_2024-02-13_at_22.03.54.jpeg	10
31	camaramz/posts/images/WhatsApp_Image_2024-02-25_at_23.07.49.jpeg	11
32	camaramz/posts/images/WhatsApp_Image_2024-02-25_at_23.36.18.jpeg	11
33	camaramz/posts/images/WhatsApp_Image_2024-02-25_at_23.37.13_1.jpeg	11
34	camaramz/posts/images/WhatsApp_Image_2024-02-25_at_23.38.16.jpeg	12
\.


--
-- Data for Name: cmz_postvideos; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_postvideos" ("id", "video", "post_id") FROM stdin;
\.


--
-- Data for Name: cmz_role; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_role" ("id", "title") FROM stdin;
1	Presidente da Câmara
\.


--
-- Data for Name: cmz_secreatarysection; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_secreatarysection" ("id", "secretary_id", "section_id") FROM stdin;
\.


--
-- Data for Name: cmz_secretary; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_secretary" ("id", "user_id") FROM stdin;
1	1
4	5
5	6
6	7
7	8
8	9
\.


--
-- Data for Name: cmz_section; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_section" ("id", "title") FROM stdin;
1	Comunicação e Imagem
\.


--
-- Data for Name: cmz_service; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_service" ("id", "name", "slug", "picture", "description") FROM stdin;
2	Atestados	atestados	camaramz/services/images/certificates.jpg	Nós atestamos junto a outra organizações sobre o teu estado dentro do Distrito de Mé-Zóchi
3	Entrega de Caixote de Lixo	entrega-de-caixote-de-lixo	camaramz/services/images/pawel-czerwinski-RkIsyD_AVvc-unsplash.jpg	Através desse website podes mandar uma mensagem e soliciitar o seu caixote de lixo.
1	Autorizações e Licenças	autorizacoes-e-licencas	camaramz/services/images/jana-shnipelson-iC3z2DkVcdE-unsplash.jpg	Pode pedir autorização para desencadear diferentes acções dentro do Distrito de Mé-Zóchi.
\.


--
-- Data for Name: cmz_team; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_team" ("id", "name", "image", "role_id") FROM stdin;
2	Anahory Espírito Santo	camaramz/team/images/inbound660959330645032735.jpg	1
\.


--
-- Data for Name: cmz_tour; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."cmz_tour" ("id", "title", "slug", "description", "location", "date", "active") FROM stdin;
2	Roça Monte Café	roca-monte-cafe	Monte Café é uma vila na ilha de São Tomé, no estado de São Tomé e Príncipe. Sua população é de 684  Fica a 4,5 km a oeste de Trindade. Situada num terreno montanhoso a 670 m de altitude, muito propícia ao cultivo do café, é sede de uma das mais antigas plantações de São Tomé, fundada em 1858.	https://www.google.com/maps/embed?pb=!1m26!1m12!1m3!1d63836.215220113496!2d6.597892972828966!3d0.30048682231460916!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m11!3e6!4m3!3m2!1d0.3030617!2d6	2023-12-02 16:02:17.644367+00	t
3	Roça Bombaim	roca-bombaim	Bombaim é uma pequena aldeia na ilha de São Tomé, em São Tomé e Príncipe. Sua população é de 18 anos. Fica a 6 km ao sul do Monte Café e a 8 km a sudoeste de Trindade. Foi criada como roça.	https://maps.app.goo.gl/WH1dRTE7FEG8zAB78	2023-12-02 16:11:05.191056+00	t
4	Jardim Botânico do Bom Sucesso	jardim-botanico-do-bom-sucesso	O Jardim Botânico do Bom Sucesso é o principal jardim botânico de São Tomé e Príncipe. É uma importante atração turística e ponto de partida para inúmeros percursos pedestres nas montanhas do interior da ilha.	https://maps.app.goo.gl/QHrdktG4cLwZCHZ87	2023-12-02 16:21:04.459247+00	t
\.

