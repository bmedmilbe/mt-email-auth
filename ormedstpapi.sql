
--
-- Data for Name: core_user; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."core_user" ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "is_staff", "is_active", "date_joined", "phone", "email", "valid", "parthner") FROM stdin;
22	pbkdf2_sha256$600000$WBBF8vxh80GqO1j5BHJi2V$l4jfbhmDjPc/aNuVaeL500BMrmXNtcxhtsM49omTM2k=	\N	f	aguilardominguez87@gmail.com	Yelena	Barroso	f	t	2023-07-21 12:22:28.308511+00	\N	aguilardominguez87@gmail.com	f 2
9	pbkdf2_sha256$600000$bHTN3Cg997NUn3qEDCDvXV$WkziTBJDbqxf6/YOBR4TyaUfbgXIoB6hFrPGjdrhTEM=	\N	f	cremildebraganca@hotmail.com	Cremilde	Bragança	f	t	2023-07-21 12:25:33.482331+00	\N	cremildebraganca@hotmail.com	f 2
21	pbkdf2_sha256$600000$uCMcNz6WpNWqwBGhqOIAH3$PgbywCpvYdP3eFfsiMn5CjqSxY8CS6YbVo5i48yUbrI=	\N	t	m.cassandra.soares@gmail.com	Miryan	Bandeira dos Prazeres Cassandra Soares	t	t	2023-07-20 13:42:00+00	9913920	m.cassandra.soares@gmail.com	t 2
15	pbkdf2_sha256$600000$chsCO0YHrlzPtxsTlTvaDP$aqzxA0B+xCmx+5XXqH9uTH0quM4xMwvr/17q3GuOM5w=	2023-12-09 05:56:40.220431+00	t	edmilbe	Edmilbe	Ramos	t	t	2023-04-12 16:11:43+00	07448019595	edmilbe@gmail.com	f 2
11	pbkdf2_sha256$600000$octow83aVZlwFNU70tA6H6$F5MGnXHnmptdybk/FgYQ2E8bHlL26YqMhqpoks1Y4sg=	\N	f	niurkasolange@gmail.com	Niurka Solange	Silveira D’Almeida	f	t	2023-09-14 06:58:30.650852+00	\N	niurkasolange@gmail.com	f 2
13	pbkdf2_sha256$600000$mpZLAOl4NCH3KjGlreOkLX$am+SMkchVKOM3Nzlk8YLK3J/shv37E8Dc8kjDQebZkA=	\N	f	bannelso@yahoo.com.br	Nelson	Bandeira	f	t	2023-09-14 07:24:07.162786+00	\N	bannelso@yahoo.com.br	f 2
14	pbkdf2_sha256$600000$D6CpoxQ66bTk0eOAu0JBvx$Jc7Yyp0VR/t92eKT4RlfCRp3FhDXKAHEIuHrJs5b774=	\N	f	eulamaquengo@gmail.com	Eula	Carvalho Maquengo	f	t	2023-09-14 09:30:15.3463+00	\N	eulamaquengo@gmail.com	f 2
17	pbkdf2_sha256$600000$TK7CxSRmWxyH00CrFcSE44$7du6lACTO2P7i+p9OUnsL8/dUmDMeY/oN4BZBzzxYRM=	\N	f	edmilbe24@gmail.com	Nome do miudeo	E este	f	t	2023-06-27 09:26:55.14852+00	\N	edmilbe24@gmail.com	f 2
18	pbkdf2_sha256$600000$Nyt91TM7MqOTd99pHVy8Ex$+/SZx1vrcbJLl1LQM5xLebqeQ166KMFHN1A5oPqdvrc=	\N	f	yelleric2@gmail.com	Yell Eric	Jordão da Costa	f	t	2023-07-14 11:17:30.059548+00	\N	yelleric2@gmail.com	f 2
19	pbkdf2_sha256$600000$Xlp1Wo5dvdkrlbO6C9CVIH$UsCgVByaJxNSeuvDR0kdmRw1qaNQmKsS/QwVIX2Nttg=	\N	f	Silvafelicia274@gmail.com	Felicia	Silva	f	t	2023-07-19 17:50:53.318288+00	\N	Silvafelicia274@gmail.com	f 2
20	pbkdf2_sha256$600000$PgCepxlGx8vYvNJ7pI8J5o$Q8LygLCPkHvX3FrHOrpjVlbhyxIttzBYiXT9tuaiWlY=	\N	t	mcelvaznas@gmail.com	Celso	Matos	t	t	2023-07-19 17:54:08+00	9804041	mcelvaznas@gmail.com	t 2
16	pbkdf2_sha256$600000$kYuLoSouCyMGttAvMEwcLk$DnTF0dpXwpRQf4lZfEZl1LT8a4me8jL1u/c0Z+LCeFo=	2023-09-28 15:05:24.665577+00	t	epinaneto@gmail.com	Eduardo	Pina Neto	t	t	2023-06-22 08:42:11+00	+2399985491	epinaneto@gmail.com	t 2
\.



COPY "public"."ormed_doctor" ("id", "birth_date", "bio", "id_number", "area_id", "country_id", "id_type_id", "level_id", "verified", "create_at", "user_id", "id_valid", "document", "picture") FROM stdin;
2	2005-05-31	hgfaduh ljhdlh	8748654	1	1	1	1	f	2023-06-27 09:26:55.372738+00	17	2023-06-27	\N	\N
6	1983-03-31	Médica cardiologista, HAM	84608	4	1	1	1	t	2023-07-20 13:42:01.082166+00	21	2023-09-20		ormed/doctors/images/Screenshot_2023-07-09-20-31-15-743-edit_com.facebook.katana2.jpg
4	1965-02-22	Licenciada em medicina desde 1985. Trabalho atualmente no serviço de pediatria do HAM	33713	1	1	1	1	t	2023-07-19 17:50:53.549846+00	19	2023-07-19		ormed/doctors/images/image0_2.jpeg
8	1986-04-24	Ginecologista	93865	5	1	1	1	t	2023-07-21 12:25:33.695368+00	9	2026-06-06		
3	1986-02-12	Yell Eric Jordão da Costa, nasceu no dia 12 de fevereiro de 1986 o distrito de Lobata em São Tomé.\r\nFilho de Antero Fernandes Nascimento da Costa e Augusta do Espírito Santo Jordão, viveu a sua infância na cidade Trindade com sua mãe mais duas irmãs. Frequentou o ensino primário, secundário  na Trindade, pré universitário no liceu Nacional, com término em 2004.	90443	1	1	1	1	t	2023-07-14 11:17:30.279806+00	18	2026-10-10	ormed/doctors/ids/IMG_20230624_062931.jpg	ormed/doctors/images/IMG_20220731_193723.jpg
7	1987-01-20	Médica especialista en Ortopedia	232311	2	1	1	1	t	2023-07-21 12:22:28.511439+00	22	2025-11-29		
1	1994-04-19	Médico de Clinica Geral formado em Cuba na Escola Latinoamericana de Medicina.	116039	1	1	1	1	t	2023-06-22 08:42:11.23482+00	16	2023-09-06		ormed/doctors/images/image.jpg
13	1985-09-11	Médica Infectologista e especialista em Vigilância em Saúde. Membro de CRM-RJ. Consultora nacional da OMS em STP para emergências de saúde pública.	91887	14	1	1	3	f	2023-09-14 09:30:15.777944+00	14	2023-09-14		ormed/doctors/images/image0.jpeg
12	2005-09-14	Licenciado em medicina em 1994\r\nEspecialização em Ginecologia e Obstetrícia em 2002	44898	5	1	1	1	f	2023-09-14 07:24:07.60242+00	13	2023-09-14		ormed/doctors/images/image0_1.jpeg
10	1990-08-22	Médica Clínica Geral formada em Cuba na Escola Latino-americana de Medicina. Atualmente trabalhando no serviço de urologia	105059	1	1	1	1	f	2023-09-14 06:58:30.847161+00	11	2025-08-26		
5	1973-04-16	Celso Matos\r\nLicenciado em Medicina em Camaguey Cuba\r\nEspecialista em Ortopedia e Traumatologia em Maputo Mocambique	62716	2	1	1	1	t	2023-07-19 17:54:08.909367+00	20	2025-05-17		ormed/doctors/images/celsomatos.jpg
\.





COPY "public"."ormed_team" ("id", "doctor_id", "role_id") FROM stdin;
2	1	1
3	4	3
4	3	12
5	6	15
6	5	6
7	12	13
8	13	4
\.


--
-- Data for Name: ormed_usersection; Type: TABLE DATA; Schema: public; Owner: yvnrmnimddzwou
--

COPY "public"."ormed_usersection" ("id", "section_id", "user_id") FROM stdin;
1	1	19
2	4	21
3	4	18
4	1	16
\.





