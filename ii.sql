--
-- Data for Name: certificates_biuldingtype; Type: TABLE DATA; Schema: public; Owner: urefl2c6bm4t5
--

COPY "public"."certificates_biuldingtype" ("id", "name", "prefix") FROM stdin;
1	Edifício	um
2	Edifício e respectivo muro de vedação	um
4	Muro de vedação	um
5	Barraca	uma
6	Quiosque	um
7	Estabelecimento comercial	um
\.

--
-- Data for Name: certificates_cemiterio; Type: TABLE DATA; Schema: public; Owner: urefl2c6bm4t5
--

COPY "public"."certificates_cemiterio" ("id", "name", "county_id") FROM stdin;
1	Trindade	1
\.


--
-- Data for Name: certificates_coval; Type: TABLE DATA; Schema: public; Owner: eurrkvbyncwetd
--

COPY "public"."certificates_coval" ("id", "nick_number", "number", "name", "date_used", "date_of_deth", "gender", "square", "closed", "selled", "cemiterio_id") FROM stdin;
6	7	541B	Aurelio de S.Baia da Costa	2013-02-19	2013-02-14	M	C	f	t	1
26	27	6B	Beatriz R. do Esp. Santo	2017-01-11	2017-01-10	F	C	f	f	1
25	26	8B	Dioner  do Sac. Mota Neto	2017-01-13	2017-01-12	M	C	f	f	1
24	25	9B	Maria da Conceição	2017-01-14	2017-01-13	F	C	f	f	1
23	24	10B	Margarida Duarte	2017-01-20	2017-01-19	F	C	f	f	1
22	23	11B	Arménio da Silva da Glória	2017-01-24	2017-01-22	M	C	f	f	1
21	22	12B	Ataíde Lázaro dos Santos	2017-01-26	2017-01-25	M	C	f	f	1
20	21	13B	Maria Tomé Vaz Filipe	2017-01-28	2017-01-27	F	C	f	f	1
19	20	14B	Ernestino Esp. S. do Nascimento	2017-01-31	2017-01-30	M	C	f	f	1
18	19	15B	Lugenia de Esp.Cravid	2017-02-03	2017-01-31	F	C	f	f	1
17	18	16B	Manuel Guadalupe de S. Lopes	2017-02-03	2017-01-31	M	C	f	f	1
16	17	18B	Domingos Graça de S. e Costa	2017-02-08	2017-02-07	M	C	f	f	1
15	16	19B	Maria Andresa Losembo	2017-02-09	2017-02-08	F	C	f	f	1
14	15	23B	Rosa do Espírito Santo	2017-02-23	2017-02-22	F	C	f	f	1
13	14	24B	Ricardina Pires D´Assunção	2017-02-27	2017-02-26	F	C	f	f	1
12	13	25B	Severina Gonçalves Af. Dias	2017-02-27	2017-02-27	M	C	f	f	1
11	12	26B	Pedro dos S. Pires Paquete	2017-02-28	2017-02-27	M	C	f	f	1
10	11	27B	Odorico Afonso	2017-03-01	2017-03-01	M	C	f	f	1
9	10	35B	Fausta Cravid Costa Alegre	2017-03-14	2017-03-13	F	C	f	f	1
8	9	41B	Maria Afonso Neto	2017-03-24	2014-03-22	F	C	f	f	1
7	8	70E	Alfredo Afonso	2018-04-16	2018-04-15	M	C	f	t	1
5	6	05L	José dos Ramos	2019-01-15	2019-01-10	M	C	f	t	1
1	1	57j	Alice Ribeiro	2019-04-16	2019-04-16	F	C	f	t	1
4	5	05L	Ateliana João de Ceita Nazaré	2020-01-07	2020-01-07	F	C	t	f	1
3	4	37L	Diogines Fernandes	2020-02-25	2020-02-23	M	C	t	f	1
2	2	42L	António Francisco Afonso Pires	2020-02-29	2020-02-26	M	C	t	f	1
27	1	264N	Manuel do Sacramento Amorím	2023-04-22	2023-04-21	M	A	t	f	1
29	5	680B	Herculano de Jesus de Ceita Vanda	2013-05-06	2013-09-04	M	A	f	f	1
30	6	1C	Maria dos Ramos da Costa Ferreira	2000-01-01	2000-12-31	F	A	f	t	1
28	4	256DC	Laurinda Simão	2011-07-13	2011-05-08	F	A	f	t	1
31	7	065J	Anibal Ferreira Viegas	2019-04-28	2019-04-27	M	A	t	f	1
32	8	208C	Juelter de Ceita Dias	2001-12-27	2001-12-25	M	A	f	t	1
33	9	368N	Maria da Conceição do E.S. Antunes	2023-10-08	2023-10-07	F	A	f	f	1
34	10	764BC	Francisca Xavier Soares	2007-06-24	2007-06-24	F	A	f	t	1
35	11	59L	Maria da Cruz Guadalupe	2020-03-24	2020-03-23	F	A	t	f	1
36	12	344N	Manuel Agostinho Neto	2023-05-07	2023-05-06	M	A	t	f	1
37	16	284C	Maria G. Julião (V. Judia)	1996-07-25	1996-07-24	F	A	f	t	1
\.
