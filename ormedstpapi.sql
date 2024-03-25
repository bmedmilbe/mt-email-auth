

COPY "public"."blog_area" ("id", "title") FROM stdin;
1	Clinica Geral
2	Ortopedia
3	Cirurgia Geral
4	Cardiologia
5	Ginecologia
6	Otorrinolaringologia
7	Oftalmologia
8	Pediatria
9	Medicina Interna
10	Psiquiatria
11	Radiologia
12	Anestesiologia
13	Gastrenterologia
14	Infectologia
\.


--
-- Data for Name: blog_country; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_country" ("id", "name") FROM stdin;
1	São Tomé e Príncipe
2	Cuba
3	Portugal
4	Brasil
5	Angola
6	Cabo verde
7	Cabo verde
8	Guiné Bissau
9	Guiné Bissau
10	Guiné Equatorial
11	Moçambique
12	Timor Leste
13	Guiné Conakry
\.


--
-- Data for Name: blog_doctor; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_doctor" ("id", "birth_date", "bio", "id_number", "area_id", "country_id", "id_type_id", "level_id", "verified", "create_at", "user_id", "id_valid", "document", "picture") FROM stdin;
2	2005-05-31	hgfaduh ljhdlh	8748654	1	1	1	1	f	2023-06-27 09:26:55.372738+00	3	2023-06-27	\N	\N
6	1983-03-31	Médica cardiologista, HAM	84608	4	1	1	1	t	2023-07-20 13:42:01.082166+00	7	2023-09-20		ormed/doctors/images/Screenshot_2023-07-09-20-31-15-743-edit_com.facebook.katana2.jpg
4	1965-02-22	Licenciada em medicina desde 1985. Trabalho atualmente no serviço de pediatria do HAM	33713	1	1	1	1	t	2023-07-19 17:50:53.549846+00	5	2023-07-19		ormed/doctors/images/image0_2.jpeg
8	1986-04-24	Ginecologista	93865	5	1	1	1	t	2023-07-21 12:25:33.695368+00	9	2026-06-06		
3	1986-02-12	Yell Eric Jordão da Costa, nasceu no dia 12 de fevereiro de 1986 o distrito de Lobata em São Tomé.\r\nFilho de Antero Fernandes Nascimento da Costa e Augusta do Espírito Santo Jordão, viveu a sua infância na cidade Trindade com sua mãe mais duas irmãs. Frequentou o ensino primário, secundário  na Trindade, pré universitário no liceu Nacional, com término em 2004.	90443	1	1	1	1	t	2023-07-14 11:17:30.279806+00	4	2026-10-10	ormed/doctors/ids/IMG_20230624_062931.jpg	ormed/doctors/images/IMG_20220731_193723.jpg
7	1987-01-20	Médica especialista en Ortopedia	232311	2	1	1	1	t	2023-07-21 12:22:28.511439+00	8	2025-11-29		
1	1994-04-19	Médico de Clinica Geral formado em Cuba na Escola Latinoamericana de Medicina.	116039	1	1	1	1	t	2023-06-22 08:42:11.23482+00	2	2023-09-06		ormed/doctors/images/image.jpg
13	1985-09-11	Médica Infectologista e especialista em Vigilância em Saúde. Membro de CRM-RJ. Consultora nacional da OMS em STP para emergências de saúde pública.	91887	14	1	1	3	f	2023-09-14 09:30:15.777944+00	14	2023-09-14		ormed/doctors/images/image0.jpeg
12	2005-09-14	Licenciado em medicina em 1994\r\nEspecialização em Ginecologia e Obstetrícia em 2002	44898	5	1	1	1	f	2023-09-14 07:24:07.60242+00	13	2023-09-14		ormed/doctors/images/image0_1.jpeg
10	1990-08-22	Médica Clínica Geral formada em Cuba na Escola Latino-americana de Medicina. Atualmente trabalhando no serviço de urologia	105059	1	1	1	1	f	2023-09-14 06:58:30.847161+00	11	2025-08-26		
5	1973-04-16	Celso Matos\r\nLicenciado em Medicina em Camaguey Cuba\r\nEspecialista em Ortopedia e Traumatologia em Maputo Mocambique	62716	2	1	1	1	t	2023-07-19 17:54:08.909367+00	6	2025-05-17		ormed/doctors/images/celsomatos.jpg
\.


--
-- Data for Name: blog_gallery; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_gallery" ("id", "title", "date", "description", "slug", "active") FROM stdin;
1	Congresso Ormed	2023-06-22 09:24:51.788398+00	Fotos do congresso f	congresso-ormed	t
\.


--
-- Data for Name: blog_idtype; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_idtype" ("id", "name") FROM stdin;
1	Bilhete de Identidade
2	Passaporte
3	Cartão de Residência Temporário
\.


--
-- Data for Name: blog_imagesgallery; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_imagesgallery" ("id", "image", "gallery_id") FROM stdin;
6	ormed/gallerys/images/cris-tagupa-9ZXHUr5aCwM-unsplash.jpg	1
\.


--
-- Data for Name: blog_law; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_law" ("id", "file", "title", "description", "slug") FROM stdin;
4	ormed/laws/documents/II_Congresso_Ordinario_-_Deliberacao_nº_1_de_7_de_Maio_de_2016_-_Atualizado.pdf	Regulamento de Inscrição e Renovação na ORMED	Deliberação n.o 1, de 7 de Maio de 2016 \r\nRegulamento de Inscrição e de Renovação da Inscrição na Ordem dos Médicos de São Tomé e Príncipe - ORMED-STP \r\nCom a publicação e a entrada em vigor Lei nº 8/2014, de 15 de Dezembro Lei que  criou a  Ordem dos Médicos de São Tomé e Príncipe (ORMED-STP) e aprovou o respetivo Estatuto foram igualmente institucionalizados os respetivos órgãos sociais, nomeadamente o Conselho Executivo da Ordem	regulamento-de-inscricao-e-renovacao-na-ormed
5	ormed/laws/documents/Aprova_o_estatuto_da_ordem_dos_medicos_de_sao_tome_e_principe_-_Leinº8_-_20.pdf	Estatuto da Ordem dos Médicos	A Ordem dos Médicos congrega todos os licenciados em Medicina, doravante designados de médicos, que, residindo no País, exerçam, queiram exercer, ou tenham exercido em qualquer regime de trabalho, a profissão médica, na observância das disposições do presente Estatuto.	estatuto-da-ordem-dos-medicos
6	ormed/laws/documents/ormed.pdf	Acta IV e V Congresso Ordinário	Regulamento n1/2018 de Estagio de Familiarização Deliberação n002/2018 de Trajo e Insígnia profissional\r\nRegulamento Geral dos Colégios de Especialidades	acta-iv-e-v-congresso-ordinario
\.


--
-- Data for Name: blog_level; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_level" ("id", "title") FROM stdin;
1	Licenciatura
2	Mestrado
3	Doutoramento
\.


--
-- Data for Name: blog_messages; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_messages" ("id", "name", "email", "subject_id", "text", "sent", "date") FROM stdin;
1	Eduardo Pina Neto	edmilbe@gmail.com	1	criterios de inscrição na ordem	t	2023-06-22 08:56:30.323855+00
2	Edmilbe Ramos	edmilbe14@hotmail.com	1	Mensagem teste!	t	2023-07-07 14:06:46.715902+00
3	Felicia Silva	silvafelicia274@gmail.com	1	Estou na rede	t	2023-07-19 18:02:29.953775+00
\.


--
-- Data for Name: blog_post; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_post" ("id", "title", "date", "picture", "active", "slug", "text_file") FROM stdin;
2	Ordem dos Médicos promete mais e melhor saúde para todos	2023-06-26 21:55:50.301543+00	ormed/posts/images/Ordem-dos-médicos-3-.jpg	t	ordem-dos-medicos-promete-mais-e-melhor-saude-para-todos	ormed/posts/documents/Ordem_dos_Médicos_promete_mais_e_melhor_saúde_para_todos.docx
3	Quem é o nosso Bastinário	2023-12-01 17:03:06.894879+00	ormed/posts/images/celsomatoss.jpg	t	quem-e-o-nosso-bastinario	ormed/posts/documents/Celso_Matos.docx
4	Formação Específica com a China	2023-12-01 17:13:09.659516+00	ormed/posts/images/Medicos-para-China-1-2-2048x1536.jpg	t	formacao-especifica-com-a-china	ormed/posts/documents/Formacao_China.docx
5	Relação Florestas-Saúde no Dia Internacional de Sociedade	2023-12-01 17:17:19.687672+00	ormed/posts/images/floresta.jpg	t	relacao-florestas-saude-no-dia-internacional-de-sociedade	ormed/posts/documents/Florestas_enfatiza_relação_benéfica_para_a_saúde.docx
6	Médicos Chineses trataram 350 alunos da Trindade	2023-12-01 19:58:09.435007+00	ormed/posts/images/china.jpeg	t	medicos-chineses-trataram-350-alunos-da-trindade	ormed/posts/documents/Médicos_Chineses_trataram_350_alunos_da_Trindade.docx
\.


--
-- Data for Name: blog_postdocument; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_postdocument" ("id", "document", "post_id") FROM stdin;
\.


--
-- Data for Name: blog_postfile; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_postfile" ("id", "file") FROM stdin;
\.


--
-- Data for Name: blog_postimages; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_postimages" ("id", "picture", "post_id") FROM stdin;
1	ormed/posts/images/Ordem-dos-médicos-.jpg	2
2	ormed/posts/images/Dr-Celso-Matos--e1629875061776.jpg	2
3	ormed/posts/images/Ordem-dos-médicos-1-e1629874989655.jpg	2
4	ormed/posts/images/Ordem-dos-médicos-1-e1629874989655.jpg	3
5	ormed/posts/images/20230823_163145-1536x691.jpg	4
6	ormed/posts/images/floresta-1.jpg	5
\.


--
-- Data for Name: blog_postvideos; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_postvideos" ("id", "video", "post_id") FROM stdin;
\.


--
-- Data for Name: blog_role; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_role" ("id", "title") FROM stdin;
1	Secretario do Conselho SNSMP
6	Bastonário
7	Vice-Bastonário
8	Secretário de Conselho Fiscal
9	Secretário de Conselho Disciplina, Ética e Deontologia Médica
10	Secretário de Conselho Ensino, Educação e Carreiras Médicas
4	1ºVogal Conselho Ensino, Educação e C. Medicas
11	2ºVogal Conselho Ensino, Educação e C. Medicas
12	3ºVogal Conselho Ensino, Educação e C. Medicas
3	2º Vogal do Conselho de SNSMP
13	1º Vogal do Conselho de SNSMP
14	3º Vogal do Conselho de SNSMP
5	Presidente do Conselho SNSMP
15	Presidente do Conselho Ensino, Educação e C. Medicas
16	Presidente do Conselho Disciplina Ética e Deontologia Médica
17	Presidente de Conselho Fiscal
2	1º Vogal do Conselho Fiscal
18	1º Vogal do Conselho de Disciplina, Ética e Deontologia Médica
\.


--
-- Data for Name: blog_section; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_section" ("id", "title") FROM stdin;
2	Conselho Fiscal
3	Conselho de Disciplina, Ética e de Deontologia Médica
4	Conselho de Ensino, Educação e Carreiras Médicas
1	Conselho para Serviço Nacional de Saúde e Exercicio de Medicina Privada
\.


--
-- Data for Name: blog_team; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_team" ("id", "doctor_id", "role_id") FROM stdin;
2	1	1
3	4	3
4	3	12
5	6	15
6	5	6
7	12	13
8	13	4
\.


--
-- Data for Name: blog_usersection; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."blog_usersection" ("id", "section_id", "user_id") FROM stdin;
1	1	5
2	4	7
3	4	4
4	1	2
\.


--
-- Data for Name: core_user; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."core_user" ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "is_staff", "is_active", "date_joined", "phone", "email", "valid") FROM stdin;
8	pbkdf2_sha256$600000$WBBF8vxh80GqO1j5BHJi2V$l4jfbhmDjPc/aNuVaeL500BMrmXNtcxhtsM49omTM2k=	\N	f	aguilardominguez87@gmail.com	Yelena	Barroso	f	t	2023-07-21 12:22:28.308511+00	\N	aguilardominguez87@gmail.com	f
9	pbkdf2_sha256$600000$bHTN3Cg997NUn3qEDCDvXV$WkziTBJDbqxf6/YOBR4TyaUfbgXIoB6hFrPGjdrhTEM=	\N	f	cremildebraganca@hotmail.com	Cremilde	Bragança	f	t	2023-07-21 12:25:33.482331+00	\N	cremildebraganca@hotmail.com	f
7	pbkdf2_sha256$600000$uCMcNz6WpNWqwBGhqOIAH3$PgbywCpvYdP3eFfsiMn5CjqSxY8CS6YbVo5i48yUbrI=	\N	t	m.cassandra.soares@gmail.com	Miryan	Bandeira dos Prazeres Cassandra Soares	t	t	2023-07-20 13:42:00+00	9913920	m.cassandra.soares@gmail.com	t
1	pbkdf2_sha256$600000$chsCO0YHrlzPtxsTlTvaDP$aqzxA0B+xCmx+5XXqH9uTH0quM4xMwvr/17q3GuOM5w=	2023-12-09 05:56:40.220431+00	t	edmilbe	Edmilbe	Ramos	t	t	2023-04-12 16:11:43+00	07448019595	edmilbe@gmail.com	f
11	pbkdf2_sha256$600000$octow83aVZlwFNU70tA6H6$F5MGnXHnmptdybk/FgYQ2E8bHlL26YqMhqpoks1Y4sg=	\N	f	niurkasolange@gmail.com	Niurka Solange	Silveira D’Almeida	f	t	2023-09-14 06:58:30.650852+00	\N	niurkasolange@gmail.com	f
13	pbkdf2_sha256$600000$mpZLAOl4NCH3KjGlreOkLX$am+SMkchVKOM3Nzlk8YLK3J/shv37E8Dc8kjDQebZkA=	\N	f	bannelso@yahoo.com.br	Nelson	Bandeira	f	t	2023-09-14 07:24:07.162786+00	\N	bannelso@yahoo.com.br	f
14	pbkdf2_sha256$600000$D6CpoxQ66bTk0eOAu0JBvx$Jc7Yyp0VR/t92eKT4RlfCRp3FhDXKAHEIuHrJs5b774=	\N	f	eulamaquengo@gmail.com	Eula	Carvalho Maquengo	f	t	2023-09-14 09:30:15.3463+00	\N	eulamaquengo@gmail.com	f
3	pbkdf2_sha256$600000$TK7CxSRmWxyH00CrFcSE44$7du6lACTO2P7i+p9OUnsL8/dUmDMeY/oN4BZBzzxYRM=	\N	f	edmilbe24@gmail.com	Nome do miudeo	E este	f	t	2023-06-27 09:26:55.14852+00	\N	edmilbe24@gmail.com	f
4	pbkdf2_sha256$600000$Nyt91TM7MqOTd99pHVy8Ex$+/SZx1vrcbJLl1LQM5xLebqeQ166KMFHN1A5oPqdvrc=	\N	f	yelleric2@gmail.com	Yell Eric	Jordão da Costa	f	t	2023-07-14 11:17:30.059548+00	\N	yelleric2@gmail.com	f
5	pbkdf2_sha256$600000$Xlp1Wo5dvdkrlbO6C9CVIH$UsCgVByaJxNSeuvDR0kdmRw1qaNQmKsS/QwVIX2Nttg=	\N	f	Silvafelicia274@gmail.com	Felicia	Silva	f	t	2023-07-19 17:50:53.318288+00	\N	Silvafelicia274@gmail.com	f
6	pbkdf2_sha256$600000$PgCepxlGx8vYvNJ7pI8J5o$Q8LygLCPkHvX3FrHOrpjVlbhyxIttzBYiXT9tuaiWlY=	\N	t	mcelvaznas@gmail.com	Celso	Matos	t	t	2023-07-19 17:54:08+00	9804041	mcelvaznas@gmail.com	t
2	pbkdf2_sha256$600000$kYuLoSouCyMGttAvMEwcLk$DnTF0dpXwpRQf4lZfEZl1LT8a4me8jL1u/c0Z+LCeFo=	2023-09-28 15:05:24.665577+00	t	epinaneto@gmail.com	Eduardo	Pina Neto	t	t	2023-06-22 08:42:11+00	+2399985491	epinaneto@gmail.com	t
\.

