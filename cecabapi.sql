


--
-- Data for Name: cecab_association; Type: TABLE DATA; Schema: public; Owner: mivtooimwtygwz
--

COPY "public"."cecab_association" ("id", "name", "registered", "address", "president_name", "number_of_associated", "picture", "district_id") FROM stdin;
42	São José	2004-01-01	Norte	x	39	cecab/blog/association_images/São_José.png	1
7	Boa Entrada	2004-01-01	Centro	x	92	cecab/blog/association_images/th_1.jpg	3
3	Agua Sampaio	2004-01-01	Centro	x	51	cecab/blog/association_images/th_1.jpg	3
5	Agua Telha	2004-01-01	Centro	x	87	cecab/blog/association_images/th_1.jpg	3
6	Benfica	2004-01-01	Centro	x	157	cecab/blog/association_images/th_1.jpg	2
8	Caldeira	2004-01-01	Centro	x	101	cecab/blog/association_images/th_1.jpg	3
9	Fernão Dias	2004-01-01	Centro	x	58	cecab/blog/association_images/th_1.jpg	3
10	Filipinas	2004-01-01	Centro	x	52	cecab/blog/association_images/th_1.jpg	2
11	Laranjeira	2004-01-01	Centro	x	72	cecab/blog/association_images/th_1.jpg	3
12	Maianço	2004-01-01	Centro	x	91	cecab/blog/association_images/th_1.jpg	3
13	Monte Macaco	2004-01-01	Centro	x	110	cecab/blog/association_images/th_1.jpg	2
14	Milagrosa	2004-01-01	Centro	x	53	cecab/blog/association_images/th_1.jpg	2
15	Pedra María	2004-01-01	Centro	x	47	cecab/blog/association_images/th_1.jpg	2
16	Plancas I	2004-01-01	Centro	x	48	cecab/blog/association_images/th_1.jpg	3
17	Plancas II	2004-01-01	Centro	x	72	cecab/blog/association_images/th_1.jpg	3
18	Prado	2004-01-01	Centro	x	78	cecab/blog/association_images/th_1.jpg	2
19	Praia das Conchas	2004-01-01	Centro	x	51	cecab/blog/association_images/th_1.jpg	3
20	Queluz	2004-01-01	Centro	x	103	cecab/blog/association_images/th_1.jpg	2
21	Rio Ouro Pequeno	2004-01-01	Centro	x	103	cecab/blog/association_images/th_1.jpg	3
22	Saltado	2004-01-01	Centro	x	50	cecab/blog/association_images/th_1.jpg	3
23	Santa Luzía	2004-01-01	Centro	x	142	cecab/blog/association_images/th_1.jpg	3
24	Vila Braga	2004-01-01	Centro	x	16	cecab/blog/association_images/th_1.jpg	3
25	Vista Alegre	2004-01-01	Centro	x	99	cecab/blog/association_images/th_1.jpg	2
26	Vanguarda Margão	2004-01-01	Centro	x	95	cecab/blog/association_images/th_1.jpg	2
27	Costa Santos	2004-01-01	Norte	x	83	cecab/blog/association_images/th_1.jpg	1
28	Generosa	2004-01-01	Norte	x	99	cecab/blog/association_images/th_1.jpg	1
29	José Luis	2004-01-01	Norte	x	34	cecab/blog/association_images/th_1.jpg	1
30	Lembá	2004-01-01	Norte	x	95	cecab/blog/association_images/th_1.jpg	1
31	María Luisa	2004-01-01	Norte	x	30	cecab/blog/association_images/th_1.jpg	1
34	Papa Fogo	2004-01-01	Norte	x	25	cecab/blog/association_images/th_1.jpg	1
40	Santa Teresa	2004-01-01	Norte	x	38	cecab/blog/association_images/Santa_Teresa.png	1
39	Sede DA/SM/RA	2004-01-01	Norte	x	91	cecab/blog/association_images/Santa_Catarina_Dona_Amaelia_São_Manuel_Rio_Ave.png	1
38	Santa Clotilde	2004-01-01	Norte	x	97	cecab/blog/association_images/Santa_Clotilde.png	1
37	Rosema	2004-01-01	Norte	x	46	cecab/blog/association_images/Rosema.png	1
36	Ribeira Palma Praia	2004-01-01	Norte	x	15	cecab/blog/association_images/Ribeira_Palma_Praia.png	1
35	Ribeira Funda	2004-01-01	Norte	x	48	cecab/blog/association_images/Ribeira_Funda.png	1
33	Malundo	2004-01-01	Norte	x	88	cecab/blog/association_images/Mulundo.png	1
4	Agua Francisca	2004-01-01	Centro	x	72	cecab/blog/association_images/Agua_Francisca.png	2
32	Monte Forte	2004-01-01	Norte	x	1	cecab/blog/association_images/Monte_Forte_Comunidade.png	1
41	Santa Jení	2004-01-01	Norte	x	33	cecab/blog/association_images/Santa_Jeny.png	1
\.

COPY "public"."core_user" ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "is_staff", "is_active", "date_joined", "phone", "email", "valid") FROM stdin;
23	pbkdf2_sha256$600000$IZjePWfdOHs9cqFvee72bd$v6jH2J6v03QB59zpq3wiMoNOfOkC+CxRR9sJaD22Zj4=	\N	f	adias.cecab@gmail.com	Antonio	Dias	t	t	2023-11-24 15:08:41+00	8758654	adias.cecab@gmail.com	f
24	pbkdf2_sha256$600000$ElMfpGOzCLfwnfer9Fdv5T$x0U8HqKVRv5rREVD3/b7TH24pMfYlZJgLP4XJQc/3AI=	2024-02-20 09:56:11.679573+00	f	direcaocecab@gmail.com	Luis	Cuba	t	t	2023-11-24 10:31:20+00	999999	direcaocecab@gmail.com	f
\.