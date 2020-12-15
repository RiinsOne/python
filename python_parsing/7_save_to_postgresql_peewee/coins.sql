--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10
-- Dumped by pg_dump version 10.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: coin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.coin (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    url text NOT NULL,
    price character varying(255) NOT NULL
);


ALTER TABLE public.coin OWNER TO postgres;

--
-- Name: coin_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.coin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.coin_id_seq OWNER TO postgres;

--
-- Name: coin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.coin_id_seq OWNED BY public.coin.id;


--
-- Name: coin id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coin ALTER COLUMN id SET DEFAULT nextval('public.coin_id_seq'::regclass);


--
-- Data for Name: coin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.coin (id, name, url, price) FROM stdin;
1	Bitcoin	https://coinmarketcap.com/currencies/bitcoin/	10081.4493504
2	Ethereum	https://coinmarketcap.com/currencies/ethereum/	178.062548639
3	XRP	https://coinmarketcap.com/currencies/ripple/	0.254652648493
4	Bitcoin Cash	https://coinmarketcap.com/currencies/bitcoin-cash/	296.893369809
5	Litecoin	https://coinmarketcap.com/currencies/litecoin/	69.2637048774
6	Tether	https://coinmarketcap.com/currencies/tether/	1.00276451305
7	EOS	https://coinmarketcap.com/currencies/eos/	3.69735282306
8	Binance Coin	https://coinmarketcap.com/currencies/binance-coin/	21.0574569051
9	Bitcoin SV	https://coinmarketcap.com/currencies/bitcoin-sv/	118.567892843
10	Monero	https://coinmarketcap.com/currencies/monero/	73.246613046
11	Cardano	https://coinmarketcap.com/currencies/cardano/	0.0450732047331
12	Stellar	https://coinmarketcap.com/currencies/stellar/	0.0588045287268
13	UNUS SED LEO	https://coinmarketcap.com/currencies/unus-sed-leo/	1.05622378818
14	Huobi Token	https://coinmarketcap.com/currencies/huobi-token/	4.15956696105
15	TRON	https://coinmarketcap.com/currencies/tron/	0.0150513823608
16	Dash	https://coinmarketcap.com/currencies/dash/	83.7185743483
17	Ethereum Classic	https://coinmarketcap.com/currencies/ethereum-classic/	6.2683560345
18	Tezos	https://coinmarketcap.com/currencies/tezos/	1.00173707309
19	IOTA	https://coinmarketcap.com/currencies/iota/	0.237467582662
20	NEO	https://coinmarketcap.com/currencies/neo/	8.79957863646
21	Chainlink	https://coinmarketcap.com/currencies/chainlink/	1.74914149981
22	Maker	https://coinmarketcap.com/currencies/maker/	482.815846102
23	Cosmos	https://coinmarketcap.com/currencies/cosmos/	2.47866493408
24	USD Coin	https://coinmarketcap.com/currencies/usd-coin/	1.00387261549
25	Ontology	https://coinmarketcap.com/currencies/ontology/	0.733248888128
26	NEM	https://coinmarketcap.com/currencies/nem/	0.0429787465407
27	Crypto.com Coin	https://coinmarketcap.com/currencies/crypto-com-coin/	0.0379331866673
28	Zcash	https://coinmarketcap.com/currencies/zcash/	44.723538949
29	Dogecoin	https://coinmarketcap.com/currencies/dogecoin/	0.00240809896862
30	HedgeTrade	https://coinmarketcap.com/currencies/hedgetrade/	0.910528071643
31	V Systems	https://coinmarketcap.com/currencies/v-systems/	0.140104978639
32	Paxos Standar...	https://coinmarketcap.com/currencies/paxos-standard-token/	1.00289244732
33	Decred	https://coinmarketcap.com/currencies/decred/	22.8424847611
34	Basic Attenti...	https://coinmarketcap.com/currencies/basic-attention-token/	0.169782789395
35	VeChain	https://coinmarketcap.com/currencies/vechain/	0.00381013202202
36	TrueUSD	https://coinmarketcap.com/currencies/trueusd/	1.00349988909
37	Qtum	https://coinmarketcap.com/currencies/qtum/	1.99073768454
38	Bitcoin Gold	https://coinmarketcap.com/currencies/bitcoin-gold/	10.2533158166
39	ZB	https://coinmarketcap.com/currencies/zb/	0.342938378599
40	OmiseGO	https://coinmarketcap.com/currencies/omisego/	1.04361840588
41	KuCoin Shares	https://coinmarketcap.com/currencies/kucoin-shares/	1.54526964771
42	Ravencoin	https://coinmarketcap.com/currencies/ravencoin/	0.0304570261521
43	BitTorrent	https://coinmarketcap.com/currencies/bittorrent/	0.000569424419638
44	Nano	https://coinmarketcap.com/currencies/nano/	0.897006869621
45	Lisk	https://coinmarketcap.com/currencies/lisk/	0.978201618076
46	Insight Chain	https://coinmarketcap.com/currencies/insight-chain/	0.331116281465
47	Augur	https://coinmarketcap.com/currencies/augur/	10.2540978634
48	Bitcoin Diamond	https://coinmarketcap.com/currencies/bitcoin-diamond/	0.60423651707
49	Holo	https://coinmarketcap.com/currencies/holo/	0.000840566505347
50	Algorand	https://coinmarketcap.com/currencies/algorand/	0.345321632284
51	Waves	https://coinmarketcap.com/currencies/waves/	1.0265523962
52	THETA	https://coinmarketcap.com/currencies/theta/	0.114087626285
53	DigiByte	https://coinmarketcap.com/currencies/digibyte/	0.0078988415162
54	MaidSafeCoin	https://coinmarketcap.com/currencies/maidsafecoin/	0.212332878883
55	ICON	https://coinmarketcap.com/currencies/icon/	0.194159628793
56	0x	https://coinmarketcap.com/currencies/0x/	0.158780591683
57	BitShares	https://coinmarketcap.com/currencies/bitshares/	0.0342847829376
58	Lambda	https://coinmarketcap.com/currencies/lambda/	0.14222793595
59	HyperCash	https://coinmarketcap.com/currencies/hypercash/	2.05369149253
60	Bytecoin	https://coinmarketcap.com/currencies/bytecoin-bcn/	0.000482709769791
61	IOST	https://coinmarketcap.com/currencies/iostoken/	0.00699507475422
62	Pundi X	https://coinmarketcap.com/currencies/pundi-x/	0.000356380668792
63	Komodo	https://coinmarketcap.com/currencies/komodo/	0.67708018067
64	Aurora	https://coinmarketcap.com/currencies/aurora/	0.0119903038457
65	Dai	https://coinmarketcap.com/currencies/dai/	0.988462314729
66	Siacoin	https://coinmarketcap.com/currencies/siacoin/	0.00181116308302
67	Bytom	https://coinmarketcap.com/currencies/bytom/	0.0745587673498
68	Verge	https://coinmarketcap.com/currencies/verge/	0.00446790477335
69	RIF Token	https://coinmarketcap.com/currencies/rif-token/	0.137162415796
70	Nash Exchange	https://coinmarketcap.com/currencies/nash-exchange/	1.84091427034
71	MonaCoin	https://coinmarketcap.com/currencies/monacoin/	0.995275893408
72	Quant	https://coinmarketcap.com/currencies/quant/	5.25678820117
73	Energi	https://coinmarketcap.com/currencies/energi/	2.898243681
74	Zilliqa	https://coinmarketcap.com/currencies/zilliqa/	0.0068038633564
75	Aeternity	https://coinmarketcap.com/currencies/aeternity/	0.204067746608
76	Enjin Coin	https://coinmarketcap.com/currencies/enjin-coin/	0.073390417604
77	Golem	https://coinmarketcap.com/currencies/golem-network-tokens/	0.0581853235628
78	Ardor	https://coinmarketcap.com/currencies/ardor/	0.0561539671469
79	Metaverse ETP	https://coinmarketcap.com/currencies/metaverse/	0.722252450272
80	Steem	https://coinmarketcap.com/currencies/steem/	0.159479042211
81	Status	https://coinmarketcap.com/currencies/status/	0.0150184150546
82	Synthetix Net...	https://coinmarketcap.com/currencies/synthetix-network-token/	0.403920759151
83	Nexo	https://coinmarketcap.com/currencies/nexo/	0.0918095395881
84	MCO	https://coinmarketcap.com/currencies/crypto-com/	3.20251641788
85	ABBC Coin	https://coinmarketcap.com/currencies/abbc-coin/	0.0879918413247
86	WINk	https://coinmarketcap.com/currencies/wink-tronbet/	0.000228349520712
87	Zcoin	https://coinmarketcap.com/currencies/zcoin/	5.26919951687
88	Beam	https://coinmarketcap.com/currencies/beam/	1.19757658445
89	Waltonchain	https://coinmarketcap.com/currencies/waltonchain/	0.978479867834
90	XMax	https://coinmarketcap.com/currencies/xmax/	0.00238167716889
91	ReddCoin	https://coinmarketcap.com/currencies/reddcoin/	0.00139203713775
92	GXChain	https://coinmarketcap.com/currencies/gxchain/	0.607572696225
93	aelf	https://coinmarketcap.com/currencies/aelf/	0.078592846422
94	Grin	https://coinmarketcap.com/currencies/grin/	1.89446859812
95	WAX	https://coinmarketcap.com/currencies/wax/	0.0409967845662
96	Ren	https://coinmarketcap.com/currencies/ren/	0.0465390255057
97	SOLVE	https://coinmarketcap.com/currencies/solve/	0.112493115878
98	Elastos	https://coinmarketcap.com/currencies/elastos/	2.27337922055
99	STASIS EURO	https://coinmarketcap.com/currencies/stasis-euro/	1.09528495716
100	Stratis	https://coinmarketcap.com/currencies/stratis/	0.351931820408
101	Dragon Coins	https://coinmarketcap.com/currencies/dragon-coins/	0.0985271524536
102	Kyber Network	https://coinmarketcap.com/currencies/kyber-network/	0.201046949806
103	Decentraland	https://coinmarketcap.com/currencies/decentraland/	0.0316800195017
104	Electroneum	https://coinmarketcap.com/currencies/electroneum/	0.00336993020042
105	Newton	https://coinmarketcap.com/currencies/newton/	0.00273896604541
106	Revain	https://coinmarketcap.com/currencies/revain/	0.0671148740959
107	Dent	https://coinmarketcap.com/currencies/dent/	0.000438886666721
108	Digitex Futures	https://coinmarketcap.com/currencies/digitex-futures/	0.0422483222497
109	Factom	https://coinmarketcap.com/currencies/factom/	3.22041005686
110	Loopring	https://coinmarketcap.com/currencies/loopring/	0.034113626343
111	QASH	https://coinmarketcap.com/currencies/qash/	0.0875233135968
112	BitCapitalVendor	https://coinmarketcap.com/currencies/bitcapitalvendor/	0.0349885302802
113	Nebulas	https://coinmarketcap.com/currencies/nebulas-token/	0.626266281341
114	NULS	https://coinmarketcap.com/currencies/nuls/	0.412668643562
115	Project Pai	https://coinmarketcap.com/currencies/project-pai/	0.0205984446361
116	Horizen	https://coinmarketcap.com/currencies/zencash/	4.02458315469
117	Fetch	https://coinmarketcap.com/currencies/fetch/	0.0551068203049
118	Matic Network	https://coinmarketcap.com/currencies/matic-network/	0.0131442122669
119	Fantom	https://coinmarketcap.com/currencies/fantom/	0.0156922790678
120	DEX	https://coinmarketcap.com/currencies/dex/	0.143539756929
121	WaykiChain	https://coinmarketcap.com/currencies/waykichain/	0.140860181116
122	DigixDAO	https://coinmarketcap.com/currencies/digixdao/	13.2944319437
123	Santiment Net...	https://coinmarketcap.com/currencies/santiment/	0.426101957511
124	Wanchain	https://coinmarketcap.com/currencies/wanchain/	0.245950486299
125	TomoChain	https://coinmarketcap.com/currencies/tomochain/	0.390463897883
126	Aion	https://coinmarketcap.com/currencies/aion/	0.0728316654477
127	Chiliz	https://coinmarketcap.com/currencies/chiliz/	0.00705296363725
128	Orbs	https://coinmarketcap.com/currencies/orbs/	0.0132676081178
129	Ark	https://coinmarketcap.com/currencies/ark/	0.217311508872
130	Loom Network	https://coinmarketcap.com/currencies/loom-network/	0.0251526962763
131	Alpha Token	https://coinmarketcap.com/currencies/alpha-token/	0.891865818856
132	LINA	https://coinmarketcap.com/currencies/lina/	0.0886604457439
133	Ignis	https://coinmarketcap.com/currencies/ignis/	0.0308907025624
134	BHPCoin	https://coinmarketcap.com/currencies/bhp-coin/	1.28388232526
135	Crypterium	https://coinmarketcap.com/currencies/crpt/	0.274779434449
136	ODEM	https://coinmarketcap.com/currencies/odem/	0.101030226758
137	Enigma	https://coinmarketcap.com/currencies/enigma/	0.304873367388
138	Bancor	https://coinmarketcap.com/currencies/bancor/	0.357407999583
139	TrueChain	https://coinmarketcap.com/currencies/truechain/	0.275196201426
140	Power Ledger	https://coinmarketcap.com/currencies/power-ledger/	0.0523476777727
141	Populous	https://coinmarketcap.com/currencies/populous/	0.409929794141
142	Bibox Token	https://coinmarketcap.com/currencies/bibox-token/	0.199453754538
143	Function X	https://coinmarketcap.com/currencies/function-x/	0.210540365931
144	Harmony	https://coinmarketcap.com/currencies/harmony/	0.00828373994564
145	Valor Token	https://coinmarketcap.com/currencies/valor-token/	1.05226125402
146	Storj	https://coinmarketcap.com/currencies/storj/	0.154636690504
147	Divi	https://coinmarketcap.com/currencies/divi/	0.0169446046657
148	Telcoin	https://coinmarketcap.com/currencies/telcoin/	0.000545552879997
149	Aragon	https://coinmarketcap.com/currencies/aragon/	0.689378403132
150	Bread	https://coinmarketcap.com/currencies/bread/	0.226540699203
151	QuarkChain	https://coinmarketcap.com/currencies/quarkchain/	0.00950952243431
152	Fusion	https://coinmarketcap.com/currencies/fusion/	0.585522100188
153	Seele	https://coinmarketcap.com/currencies/seele/	0.0286853659135
154	Moeda Loyalty...	https://coinmarketcap.com/currencies/moeda-loyalty-points/	1.01488722059
155	CRYPTO20	https://coinmarketcap.com/currencies/c20/	0.483702779852
156	Cocos-BCX	https://coinmarketcap.com/currencies/cocos-bcx/	0.0012292550003
157	Perlin	https://coinmarketcap.com/currencies/perlin/	0.0717221434762
158	Metal	https://coinmarketcap.com/currencies/metal/	0.375622009015
159	IoTeX	https://coinmarketcap.com/currencies/iotex/	0.00446832233215
160	Arcblock	https://coinmarketcap.com/currencies/arcblock/	0.186444543515
161	Eidoo	https://coinmarketcap.com/currencies/eidoo/	0.343411549743
162	RealTract	https://coinmarketcap.com/currencies/realtract/	0.00170410301316
163	Hyperion	https://coinmarketcap.com/currencies/hyperion/	0.056352117907
164	RChain	https://coinmarketcap.com/currencies/rchain/	0.0476865106669
165	Blackmoon	https://coinmarketcap.com/currencies/blackmoon/	0.445307741272
166	TTC	https://coinmarketcap.com/currencies/ttc/	0.0503657624791
167	Celer Network	https://coinmarketcap.com/currencies/celer-network/	0.00552004035146
168	CyberMiles	https://coinmarketcap.com/currencies/cybermiles/	0.0215858507144
169	PIVX	https://coinmarketcap.com/currencies/pivx/	0.300985958347
170	Theta Fuel	https://coinmarketcap.com/currencies/theta-fuel/	0.00443007528948
171	FunFair	https://coinmarketcap.com/currencies/funfair/	0.00257316537248
172	Groestlcoin	https://coinmarketcap.com/currencies/groestlcoin/	0.223663325646
173	Credits	https://coinmarketcap.com/currencies/credits/	0.0980288325668
174	Centrality	https://coinmarketcap.com/currencies/centrality/	0.019889204414
175	Litecoin Cash	https://coinmarketcap.com/currencies/litecoin-cash/	0.0244782655312
176	Content Value...	https://coinmarketcap.com/currencies/content-value-network/	0.0295906326231
177	iExec RLC	https://coinmarketcap.com/currencies/rlc/	0.195038886476
178	Gnosis	https://coinmarketcap.com/currencies/gnosis-gno/	14.1848728446
179	ZrCoin	https://coinmarketcap.com/currencies/zrcoin/	3.36874941674
180	Civic	https://coinmarketcap.com/currencies/civic/	0.044668741097
181	BnkToTheFuture	https://coinmarketcap.com/currencies/bnktothefuture/	0.0208392281235
182	Polymath	https://coinmarketcap.com/currencies/polymath-network/	0.0338883093975
183	Robotina	https://coinmarketcap.com/currencies/robotina/	0.0494480567519
184	Davinci Coin	https://coinmarketcap.com/currencies/davinci-coin/	0.00407245023129
185	EDC Blockchain	https://coinmarketcap.com/currencies/edc-blockchain/	0.00538805609543
186	Bitcoin Rhodium	https://coinmarketcap.com/currencies/bitcoin-rhodium/	17.3081703372
187	Thunder Token	https://coinmarketcap.com/currencies/thunder-token/	0.0049113118987
188	SingularityNET	https://coinmarketcap.com/currencies/singularitynet/	0.0263855693181
189	UGAS	https://coinmarketcap.com/currencies/ugas/	0.0828444927961
190	Syscoin	https://coinmarketcap.com/currencies/syscoin/	0.0249683225426
191	Nexus	https://coinmarketcap.com/currencies/nexus/	0.217673513542
192	Gas	https://coinmarketcap.com/currencies/gas/	1.37520422292
193	Egretia	https://coinmarketcap.com/currencies/egretia/	0.00329637296992
194	Vertcoin	https://coinmarketcap.com/currencies/vertcoin/	0.268938725194
195	MediBloc [ERC20]	https://coinmarketcap.com/currencies/medx/	0.00402550996318
196	Nxt	https://coinmarketcap.com/currencies/nxt/	0.013572940869
197	IoT Chain	https://coinmarketcap.com/currencies/iot-chain/	0.159668196733
198	Einsteinium	https://coinmarketcap.com/currencies/einsteinium/	0.0584479253944
199	Ankr	https://coinmarketcap.com/currencies/ankr/	0.0031592026731
200	High Performa...	https://coinmarketcap.com/currencies/high-performance-blockchain/	0.288679279875
201	Atlantis Blue...	https://coinmarketcap.com/currencies/atlantis-blue-digital-token/	2.58396203866
202	INO COIN	https://coinmarketcap.com/currencies/ino-coin/	1.9853083525
203	ThoreNext	https://coinmarketcap.com/currencies/thorenext/	9.70828323151
204	ThoreCoin	https://coinmarketcap.com/currencies/thorecoin/	1813.12614824
205	Karatgold Coin	https://coinmarketcap.com/currencies/karatgold-coin/	0.0369327629421
206	EDUCare	https://coinmarketcap.com/currencies/educare/	0.162413836913
207	NEXT	https://coinmarketcap.com/currencies/next/	2.35023364368
208	Clipper Coin	https://coinmarketcap.com/currencies/clipper-coin/	0.0293013413959
209	Mixin	https://coinmarketcap.com/currencies/mixin/	214.317674616
210	Oasis City	https://coinmarketcap.com/currencies/oasis-city/	0.0442331118441
211	Maximine Coin	https://coinmarketcap.com/currencies/maximine-coin/	0.0495894812491
212	ETERNAL TOKEN	https://coinmarketcap.com/currencies/eternal-token/	0.836027814699
213	Bitbook Gambling	https://coinmarketcap.com/currencies/bitbook-gambling/	0.205164118833
214	Flexacoin	https://coinmarketcap.com/currencies/flexacoin/	0.00335000569622
215	Beldex	https://coinmarketcap.com/currencies/beldex/	0.0700187166448
216	Qubitica	https://coinmarketcap.com/currencies/qubitica/	32.5261171171
217	OKB	https://coinmarketcap.com/currencies/okb/	2.80607807286
218	Wixlar	https://coinmarketcap.com/currencies/wixlar/	0.023456192122
219	1irstcoin	https://coinmarketcap.com/currencies/1irstcoin/	2.18266007468
220	Japan Content...	https://coinmarketcap.com/currencies/japan-content-token/	0.161522375365
221	Ecoreal Estate	https://coinmarketcap.com/currencies/ecoreal-estate/	0.216586849917
222	Cryptoindex.c...	https://coinmarketcap.com/currencies/cryptoindex-com-100/	0.71736240326
223	Dynamic Tradi...	https://coinmarketcap.com/currencies/dynamic-trading-rights/	0.0274915334479
224	Vitae	https://coinmarketcap.com/currencies/vitae/	2.1458394594
225	PLATINCOIN	https://coinmarketcap.com/currencies/platincoin/	7.65691444619
226	Bankera	https://coinmarketcap.com/currencies/bankera/	0.00151093891247
227	Buggyra Coin ...	https://coinmarketcap.com/currencies/buggyra-coin-zero/	0.0181975039578
228	CryptoVerific...	https://coinmarketcap.com/currencies/cryptoverificationcoin/	59.8681159348
229	Bit-Z Token	https://coinmarketcap.com/currencies/bit-z-token/	0.251471741678
230	Litex	https://coinmarketcap.com/currencies/litex/	0.0352447981393
231	BHEX Token	https://coinmarketcap.com/currencies/bhex-token/	0.0563807715676
232	VestChain	https://coinmarketcap.com/currencies/vestchain/	0.00453308184957
233	BQT	https://coinmarketcap.com/currencies/bqt/	0.0826502292411
234	Atlas Protocol	https://coinmarketcap.com/currencies/atlas-protocol/	0.011777401092
235	FTX Token	https://coinmarketcap.com/currencies/ftx-token/	1.1823882183
236	USDK	https://coinmarketcap.com/currencies/usdk/	0.99235473374
237	BitcoinHD	https://coinmarketcap.com/currencies/bitcoinhd/	14.6119231059
238	LATOKEN	https://coinmarketcap.com/currencies/latoken/	0.0717602718632
239	Veritaseum	https://coinmarketcap.com/currencies/veritaseum/	12.4025348594
240	MOAC	https://coinmarketcap.com/currencies/moac/	0.392794486151
241	IPChain	https://coinmarketcap.com/currencies/ipchain/	0.312785895136
242	MB8 Coin	https://coinmarketcap.com/currencies/mb8-coin/	0.0413450756391
243	Tratin	https://coinmarketcap.com/currencies/tratin/	0.00021177559253
244	BTU Protocol	https://coinmarketcap.com/currencies/btu-protocol/	0.322333537465
245	PRIZM	https://coinmarketcap.com/currencies/prizm/	0.421433738856
246	Safe	https://coinmarketcap.com/currencies/safe/	1.05885591424
247	GreenPower	https://coinmarketcap.com/currencies/greenpower/	0.00676845089463
248	General Atten...	https://coinmarketcap.com/currencies/general-attention-currency/	2.13483007655
249	AgaveCoin	https://coinmarketcap.com/currencies/agavecoin/	0.054445026511
250	pEOS	https://coinmarketcap.com/currencies/peos/	0.0249822526791
251	Silverway	https://coinmarketcap.com/currencies/silverway/	0.205354110108
252	Ultiledger	https://coinmarketcap.com/currencies/ultiledger/	0.0302889117723
253	Bitcoin 2	https://coinmarketcap.com/currencies/bitcoin2/	1.07075171977
254	UnlimitedIP	https://coinmarketcap.com/currencies/unlimitedip/	0.0149858103795
255	Spectre.ai Di...	https://coinmarketcap.com/currencies/spectre-dividend/	0.221128317947
256	Carry	https://coinmarketcap.com/currencies/carry/	0.00732504067444
257	DAPS Token	https://coinmarketcap.com/currencies/daps-token/	0.00031355736425
258	Unobtanium	https://coinmarketcap.com/currencies/unobtanium/	80.5851432368
259	MicroBitcoin	https://coinmarketcap.com/currencies/microbitcoin/	8.61965950418e-05
260	botXcoin	https://coinmarketcap.com/currencies/botxcoin/	0.00952441515521
261	Obyte	https://coinmarketcap.com/currencies/obyte/	21.5773133439
262	United Trader...	https://coinmarketcap.com/currencies/uttoken/	0.39923634589
263	Cryptonex	https://coinmarketcap.com/currencies/cryptonex/	0.265691046877
264	SaluS	https://coinmarketcap.com/currencies/salus/	14.2484518359
265	CasinoCoin	https://coinmarketcap.com/currencies/casinocoin/	0.000364434360887
266	PlayChip	https://coinmarketcap.com/currencies/playchip/	0.00100414298337
267	Envion	https://coinmarketcap.com/currencies/envion/	0.116753521158
268	Bitrue Coin	https://coinmarketcap.com/currencies/bitrue-coin/	0.0989966101974
269	DDKoin	https://coinmarketcap.com/currencies/ddkoin/	8.04751161306
270	Apollo Currency	https://coinmarketcap.com/currencies/apollo-currency/	0.000926800667321
271	Clams	https://coinmarketcap.com/currencies/clams/	3.57095194895
272	Monolith	https://coinmarketcap.com/currencies/monolith/	0.420084572446
273	CommerceBlock	https://coinmarketcap.com/currencies/commerceblock/	0.0718205369825
274	GNY	https://coinmarketcap.com/currencies/gny/	0.0662578088053
275	Cortex	https://coinmarketcap.com/currencies/cortex/	0.0832684182204
276	Humanscape	https://coinmarketcap.com/currencies/humanscape/	0.000304739941523
277	Aladdin	https://coinmarketcap.com/currencies/aladdin/	0.0003932980938
278	TenX	https://coinmarketcap.com/currencies/tenx/	0.105588885
279	GoWithMi	https://coinmarketcap.com/currencies/gowithmi/	0.00464536145495
280	Matrix AI Net...	https://coinmarketcap.com/currencies/matrix-ai-network/	0.0665605032791
281	Burst	https://coinmarketcap.com/currencies/burst/	0.00593637765117
282	Contentos	https://coinmarketcap.com/currencies/contentos/	0.0197413248112
283	Tierion	https://coinmarketcap.com/currencies/tierion/	0.0275947129593
284	Mithril	https://coinmarketcap.com/currencies/mithril/	0.0173694679815
285	Tripio	https://coinmarketcap.com/currencies/tripio/	0.00314237930154
286	Particl	https://coinmarketcap.com/currencies/particl/	1.45675048837
287	Proton Token	https://coinmarketcap.com/currencies/proton-token/	0.00142083775543
288	B2BX	https://coinmarketcap.com/currencies/b2bx/	0.688253761622
289	BitKan	https://coinmarketcap.com/currencies/bitkan/	0.00284428847489
290	Elrond	https://coinmarketcap.com/currencies/elrond/	0.00186736409232
291	OTOCASH	https://coinmarketcap.com/currencies/otocash/	0.522073842337
292	Diamond Platf...	https://coinmarketcap.com/currencies/diamond-platform-token/	12.5438716967
293	FirstBlood	https://coinmarketcap.com/currencies/firstblood/	0.127995730142
294	Aencoin	https://coinmarketcap.com/currencies/aencoin/	0.0417906401997
295	Everipedia	https://coinmarketcap.com/currencies/everipedia/	0.00241965569552
296	PressOne	https://coinmarketcap.com/currencies/pressone/	0.0381979481182
297	Quantum Resis...	https://coinmarketcap.com/currencies/quantum-resistant-ledger/	0.156123601942
298	DxChain Token	https://coinmarketcap.com/currencies/dxchain-token/	0.000232704737225
299	ILCoin	https://coinmarketcap.com/currencies/ilcoin/	0.0406444942569
300	Ruff	https://coinmarketcap.com/currencies/ruff/	0.0108349000569
301	Dragonchain	https://coinmarketcap.com/currencies/dragonchain/	0.0438076372546
302	ProximaX	https://coinmarketcap.com/currencies/proximax/	0.00170562351733
303	Metadium	https://coinmarketcap.com/currencies/metadium/	0.00833335133469
304	Mainframe	https://coinmarketcap.com/currencies/mainframe/	0.00117565801353
305	PayPie	https://coinmarketcap.com/currencies/paypie/	0.125562145705
306	Noah Coin	https://coinmarketcap.com/currencies/noah-coin/	0.000314478359559
307	Time New Bank	https://coinmarketcap.com/currencies/time-new-bank/	0.00355080301557
308	SALT	https://coinmarketcap.com/currencies/salt/	0.127432273337
309	Hubii Network	https://coinmarketcap.com/currencies/hubii-network/	0.671960394498
310	Origo	https://coinmarketcap.com/currencies/origo/	0.0267842827183
311	MediBloc [QRC20]	https://coinmarketcap.com/currencies/medibloc/	0.00341340335448
312	All Sports	https://coinmarketcap.com/currencies/all-sports/	0.00669994931206
313	Reserve Rights	https://coinmarketcap.com/currencies/reserve-rights/	0.00237548592891
314	Gifto	https://coinmarketcap.com/currencies/gifto/	0.0164976811294
315	Tael	https://coinmarketcap.com/currencies/tael/	0.171881255629
316	Storm	https://coinmarketcap.com/currencies/storm/	0.00158562034433
317	Kin	https://coinmarketcap.com/currencies/kin/	1.28803654083e-05
318	Cindicator	https://coinmarketcap.com/currencies/cindicator/	0.00665645967588
319	HYCON	https://coinmarketcap.com/currencies/hycon/	0.0048354695473
320	U Network	https://coinmarketcap.com/currencies/u-network/	0.000959321661652
321	IRISnet	https://coinmarketcap.com/currencies/irisnet/	0.0250118959398
322	Wagerr	https://coinmarketcap.com/currencies/wagerr/	0.0466465884325
323	Constellation	https://coinmarketcap.com/currencies/constellation/	0.0110545953852
324	Namecoin	https://coinmarketcap.com/currencies/namecoin/	0.636896419717
325	Dentacoin	https://coinmarketcap.com/currencies/dentacoin/	2.84574169623e-05
326	Contents Prot...	https://coinmarketcap.com/currencies/contents-protocol/	0.00331474349302
327	UTRUST	https://coinmarketcap.com/currencies/utrust/	0.0203558888177
328	Cred	https://coinmarketcap.com/currencies/libra-credit/	0.015676819935
329	Levolution	https://coinmarketcap.com/currencies/levolution/	0.405752462369
330	ZTCoin	https://coinmarketcap.com/currencies/ztcoin/	0.0411262634007
331	Data Transact...	https://coinmarketcap.com/currencies/data-transaction-token/	0.0454815359192
332	Insolar	https://coinmarketcap.com/currencies/insolar/	0.275198892033
333	Lightning Bit...	https://coinmarketcap.com/currencies/lightning-bitcoin/	2.31621330473
334	Restart Energ...	https://coinmarketcap.com/currencies/restart-energy-mwat/	0.0197462997385
335	LTO Network	https://coinmarketcap.com/currencies/lto-network/	0.0481065910324
336	TOP	https://coinmarketcap.com/currencies/top/	0.00305225654358
337	Everex	https://coinmarketcap.com/currencies/everex/	0.388396419685
338	VeriDocGlobal	https://coinmarketcap.com/currencies/veridocglobal/	0.00111690643886
339	GoChain	https://coinmarketcap.com/currencies/gochain/	0.0110950417381
340	Blox	https://coinmarketcap.com/currencies/blox/	0.0127252162774
341	Hydro	https://coinmarketcap.com/currencies/hydrogen/	0.000790114745648
342	Aergo	https://coinmarketcap.com/currencies/aergo/	0.0822941765394
343	Po.et	https://coinmarketcap.com/currencies/poet/	0.00272103402036
344	Aeon	https://coinmarketcap.com/currencies/aeon/	0.538492010157
345	Gemini Dollar	https://coinmarketcap.com/currencies/gemini-dollar/	1.00154921933
346	SIX	https://coinmarketcap.com/currencies/six/	0.030894681907
347	NKN	https://coinmarketcap.com/currencies/nkn/	0.024009264632
348	Skycoin	https://coinmarketcap.com/currencies/skycoin/	0.52394646226
349	DEW	https://coinmarketcap.com/currencies/dew/	0.0806593116044
350	Peercoin	https://coinmarketcap.com/currencies/peercoin/	0.322616358035
351	PumaPay	https://coinmarketcap.com/currencies/pumapay/	0.000346066292804
352	Dusk Network	https://coinmarketcap.com/currencies/dusk-network/	0.0930139353106
353	Amoveo	https://coinmarketcap.com/currencies/amoveo/	123.514182387
354	Streamr DATAcoin	https://coinmarketcap.com/currencies/streamr-datacoin/	0.0119563372996
355	Cosmo Coin	https://coinmarketcap.com/currencies/cosmo-coin/	0.0120033098435
356	Raiden Networ...	https://coinmarketcap.com/currencies/raiden-network-token/	0.159013718651
357	VITE	https://coinmarketcap.com/currencies/vite/	0.0190247403054
358	OST	https://coinmarketcap.com/currencies/ost/	0.0117582935046
359	Locus Chain	https://coinmarketcap.com/currencies/locus-chain/	0.010043031515
360	Linkey	https://coinmarketcap.com/currencies/linkey/	0.153353476893
361	Incent	https://coinmarketcap.com/currencies/incent/	0.166591543465
362	Request	https://coinmarketcap.com/currencies/request/	0.0104931124282
363	THEKEY	https://coinmarketcap.com/currencies/thekey/	0.00150546804613
364	Everus	https://coinmarketcap.com/currencies/everus/	0.0165322426262
365	#MetaHash	https://coinmarketcap.com/currencies/metahash/	0.00543258926204
366	Nectar	https://coinmarketcap.com/currencies/nectar/	0.0905835329456
367	SwissBorg	https://coinmarketcap.com/currencies/swissborg/	0.012939884826
368	Quantstamp	https://coinmarketcap.com/currencies/quantstamp/	0.0119873811509
369	Ethos	https://coinmarketcap.com/currencies/ethos/	0.0754974918977
370	NavCoin	https://coinmarketcap.com/currencies/nav-coin/	0.110817486568
371	TaaS	https://coinmarketcap.com/currencies/taas/	0.891554418781
372	Eligma Token	https://coinmarketcap.com/currencies/eligma-token/	0.0359901867649
373	Mindexcoin	https://coinmarketcap.com/currencies/mindexcoin/	0.0104758399676
374	Neblio	https://coinmarketcap.com/currencies/neblio/	0.47621765155
375	Force Protocol	https://coinmarketcap.com/currencies/force-protocol/	0.0304037052923
376	IDEX	https://coinmarketcap.com/currencies/idex/	0.0156542152061
674	OLXA	https://coinmarketcap.com/currencies/olxa/	0.00157341901397
377	TokenClub	https://coinmarketcap.com/currencies/tokenclub/	0.0144227198358
378	CyberVein	https://coinmarketcap.com/currencies/cybervein/	0.00654436667873
379	Tokenomy	https://coinmarketcap.com/currencies/tokenomy/	0.0346971532533
380	Morpheus.Network	https://coinmarketcap.com/currencies/morpheus-network/	0.211149147453
381	ContentBox	https://coinmarketcap.com/currencies/contentbox/	0.00744314441188
382	Achain	https://coinmarketcap.com/currencies/achain/	0.00722807669048
383	OneRoot Network	https://coinmarketcap.com/currencies/oneroot-network/	0.0241359700736
384	Odyssey	https://coinmarketcap.com/currencies/odyssey/	0.00102489729938
385	Propy	https://coinmarketcap.com/currencies/propy/	0.143571799678
386	LockTrip	https://coinmarketcap.com/currencies/lockchain/	0.45315995148
387	MovieBloc	https://coinmarketcap.com/currencies/moviebloc/	0.0018151069674
388	Bluzelle	https://coinmarketcap.com/currencies/bluzelle/	0.0320255415496
389	Pillar	https://coinmarketcap.com/currencies/pillar/	0.0258183575557
390	Dropil	https://coinmarketcap.com/currencies/dropil/	0.000294168764714
391	DigitalNote	https://coinmarketcap.com/currencies/digitalnote/	0.000906563074119
392	Sport and Lei...	https://coinmarketcap.com/currencies/sport-and-leisure/	0.00995530983399
393	AXE	https://coinmarketcap.com/currencies/axe/	1.3339641993
394	doc.com Token	https://coinmarketcap.com/currencies/doc-com-token/	0.00933615728669
395	VeriBlock	https://coinmarketcap.com/currencies/veriblock/	0.0130660879013
396	APIS	https://coinmarketcap.com/currencies/apis/	0.000738689086521
397	Nucleus Vision	https://coinmarketcap.com/currencies/nucleus-vision/	0.00113040326127
398	REPO	https://coinmarketcap.com/currencies/repo/	0.0595466323702
399	bitCNY	https://coinmarketcap.com/currencies/bitcny/	0.141153314526
400	NewYork Exchange	https://coinmarketcap.com/currencies/newyork-exchange/	4.82392284662
401	Ripio Credit ...	https://coinmarketcap.com/currencies/ripio-credit-network/	0.0128717882541
402	Rotharium	https://coinmarketcap.com/currencies/rotharium/	1.93195338022
403	Blocknet	https://coinmarketcap.com/currencies/blocknet/	1.0510926332
404	Cube	https://coinmarketcap.com/currencies/cube/	0.000943927019944
405	Ocean Protocol	https://coinmarketcap.com/currencies/ocean-protocol/	0.0210324812543
406	Scry.info	https://coinmarketcap.com/currencies/scryinfo/	0.014009109362
407	ZelCash	https://coinmarketcap.com/currencies/zelcash/	0.0832063651039
408	Measurable Da...	https://coinmarketcap.com/currencies/measurable-data-token/	0.0112751908997
409	Numeraire	https://coinmarketcap.com/currencies/numeraire/	4.57934721092
410	DATA	https://coinmarketcap.com/currencies/data/	0.000629417587753
411	Monetha	https://coinmarketcap.com/currencies/monetha/	0.0152811281762
412	Stakenet	https://coinmarketcap.com/currencies/stakenet/	0.0698155680513
413	DeepBrain Chain	https://coinmarketcap.com/currencies/deepbrain-chain/	0.00191045033849
414	Metronome	https://coinmarketcap.com/currencies/metronome/	0.636066316988
415	Steem Dollars	https://coinmarketcap.com/currencies/steem-dollars/	0.801423023573
416	NaPoleonX	https://coinmarketcap.com/currencies/napoleonx/	0.277046298079
417	FLO	https://coinmarketcap.com/currencies/flo/	0.0390529087866
418	Moss Coin	https://coinmarketcap.com/currencies/moss-coin/	0.0200362265582
419	Wrapped Bitcoin	https://coinmarketcap.com/currencies/wrapped-bitcoin/	10182.9306526
420	WhiteCoin	https://coinmarketcap.com/currencies/whitecoin/	0.0222303499979
421	Elitium	https://coinmarketcap.com/currencies/elitium/	1.15614388302
422	Artfinity	https://coinmarketcap.com/currencies/artfinity/	0.0485511602697
423	AdEx	https://coinmarketcap.com/currencies/adx-net/	0.0773297631688
424	Morpheus Labs	https://coinmarketcap.com/currencies/morpheus-labs/	0.0162495705201
425	Bezant	https://coinmarketcap.com/currencies/bezant/	0.00701202258335
426	Safex Token	https://coinmarketcap.com/currencies/safex-token/	0.00483500306197
427	Zipper	https://coinmarketcap.com/currencies/zip/	0.000345178842346
428	Jibrel Network	https://coinmarketcap.com/currencies/jibrel-network/	0.0327104549325
429	ParkinGo	https://coinmarketcap.com/currencies/parkingo/	0.368727118069
430	TERA	https://coinmarketcap.com/currencies/tera/	0.0065182168396
431	SmartMesh	https://coinmarketcap.com/currencies/smartmesh/	0.00410438646852
432	IntelliShare	https://coinmarketcap.com/currencies/intellishare/	0.0316595023042
433	Pivot Token	https://coinmarketcap.com/currencies/pivot-token/	0.00106486763376
434	TrustVerse	https://coinmarketcap.com/currencies/trustverse/	0.0240702757873
435	USDQ	https://coinmarketcap.com/currencies/usdq/	0.98915977087
436	Red Pulse Pho...	https://coinmarketcap.com/currencies/red-pulse/	0.00646808695089
437	OAX	https://coinmarketcap.com/currencies/oax/	0.072132271823
438	Asch	https://coinmarketcap.com/currencies/asch/	0.0580185293963
439	Loki	https://coinmarketcap.com/currencies/loki/	0.126984617035
440	QunQun	https://coinmarketcap.com/currencies/qunqun/	0.00833757203211
441	FOAM	https://coinmarketcap.com/currencies/foam/	0.0190576205152
442	Viacoin	https://coinmarketcap.com/currencies/viacoin/	0.230120373211
443	CWV Chain	https://coinmarketcap.com/currencies/cwv-chain/	0.00150433315305
444	Ether Zero	https://coinmarketcap.com/currencies/ether-zero/	0.0320114452614
445	BLOCKv	https://coinmarketcap.com/currencies/blockv/	0.00197984535799
446	Cryptaur	https://coinmarketcap.com/currencies/cryptaur/	0.000537280005751
447	Electra	https://coinmarketcap.com/currencies/electra/	0.000183518666907
448	Emercoin	https://coinmarketcap.com/currencies/emercoin/	0.116977522452
449	Hydro Protocol	https://coinmarketcap.com/currencies/hydro-protocol/	0.00732976185158
450	DAO.Casino	https://coinmarketcap.com/currencies/dao-casino/	0.0307178625721
451	Cashaa	https://coinmarketcap.com/currencies/cashaa/	0.00673885866512
452	OVCODE	https://coinmarketcap.com/currencies/ovcode/	0.115266407037
453	Travala.com	https://coinmarketcap.com/currencies/travala/	0.112436502452
454	TCASH	https://coinmarketcap.com/currencies/tcash/	0.142296355594
455	Digix Gold Token	https://coinmarketcap.com/currencies/digix-gold-token/	47.9911990886
456	Genesis Vision	https://coinmarketcap.com/currencies/genesis-vision/	1.12281511538
457	Invictus Hype...	https://coinmarketcap.com/currencies/invictus-hyperion-fund/	0.0415851221635
458	DMarket	https://coinmarketcap.com/currencies/dmarket/	0.0863514870045
459	XYO	https://coinmarketcap.com/currencies/xyo/	0.000585443954203
460	Counterparty	https://coinmarketcap.com/currencies/counterparty/	1.8561312656
461	SwftCoin	https://coinmarketcap.com/currencies/swftcoin/	0.00132403468343
462	BOX Token	https://coinmarketcap.com/currencies/box-token/	0.0482015670799
463	SIRIN LABS Token	https://coinmarketcap.com/currencies/sirin-labs-token/	0.00976901188195
464	Polybius	https://coinmarketcap.com/currencies/polybius/	1.20907007633
465	Swarm	https://coinmarketcap.com/currencies/swarm-fund/	0.0611984088002
466	NIX	https://coinmarketcap.com/currencies/nix/	0.110161705365
467	BlockMason Cr...	https://coinmarketcap.com/currencies/blockmason/	0.0412058555051
468	Chimpion	https://coinmarketcap.com/currencies/chimpion/	0.14907733838
469	Bitcore	https://coinmarketcap.com/currencies/bitcore/	0.269689719561
470	Content Neutr...	https://coinmarketcap.com/currencies/content-neutrality-network/	0.000119411718152
471	Own	https://coinmarketcap.com/currencies/own/	0.0586333022932
472	TokenPay	https://coinmarketcap.com/currencies/tokenpay/	0.285795954675
473	Lympo	https://coinmarketcap.com/currencies/lympo/	0.00561328935137
474	Lendingblock	https://coinmarketcap.com/currencies/lendingblock/	0.00596673393522
475	Smartshare	https://coinmarketcap.com/currencies/smartshare/	0.000994269499951
476	SmartCash	https://coinmarketcap.com/currencies/smartcash/	0.00324087050794
477	DADI	https://coinmarketcap.com/currencies/dadi/	0.061355769837
478	Melon	https://coinmarketcap.com/currencies/melon/	3.8022083001
479	BOScoin	https://coinmarketcap.com/currencies/boscoin/	0.00679339762639
480	Jewel	https://coinmarketcap.com/currencies/jewel/	0.082176758226
481	Cajutel	https://coinmarketcap.com/currencies/cajutel/	3.31638588851
482	Delphy	https://coinmarketcap.com/currencies/delphy/	0.071952846823
483	BitMart Token	https://coinmarketcap.com/currencies/bitmart-token/	0.0273601642118
484	MenaPay	https://coinmarketcap.com/currencies/menapay/	0.0497464640428
485	Primas	https://coinmarketcap.com/currencies/primas/	0.0842795024105
486	Pepe Cash	https://coinmarketcap.com/currencies/pepe-cash/	0.00621803973977
487	ImageCoin	https://coinmarketcap.com/currencies/imagecoin/	0.3438275408
488	SingularDTV	https://coinmarketcap.com/currencies/singulardtv/	0.00725672203377
489	Dero	https://coinmarketcap.com/currencies/dero/	0.525760080119
490	Aave	https://coinmarketcap.com/currencies/aave/	0.00383664244776
491	OneLedger	https://coinmarketcap.com/currencies/oneledger/	0.0125412067146
492	Rublix	https://coinmarketcap.com/currencies/rublix/	0.207703673204
493	VIBE	https://coinmarketcap.com/currencies/vibe/	0.016507335471
494	Hi Mutual Soc...	https://coinmarketcap.com/currencies/hi-mutual-society/	0.0104850137674
495	Metrix Coin	https://coinmarketcap.com/currencies/metrix-coin/	0.000302187691373
496	Spectrecoin	https://coinmarketcap.com/currencies/spectrecoin/	0.188773667213
497	Tarush	https://coinmarketcap.com/currencies/tarush/	0.000704998036
498	district0x	https://coinmarketcap.com/currencies/district0x/	0.00704406914962
499	BlackCoin	https://coinmarketcap.com/currencies/blackcoin/	0.0710882985852
500	Genaro Network	https://coinmarketcap.com/currencies/genaro-network/	0.0163794434173
501	Genaro Network	https://coinmarketcap.com/currencies/genaro-network/	0.0163794434173
502	Endor Protocol	https://coinmarketcap.com/currencies/endor-protocol/	0.00540707552384
503	Refereum	https://coinmarketcap.com/currencies/refereum/	0.00101964263113
504	Global Social...	https://coinmarketcap.com/currencies/global-social-chain/	0.00764431801724
505	Boolberry	https://coinmarketcap.com/currencies/boolberry/	0.314493585696
506	Darico Ecosys...	https://coinmarketcap.com/currencies/darcio-ecosystem-coin/	0.0801490534518
507	Bitsdaq	https://coinmarketcap.com/currencies/bitsdaq/	0.00227573848935
508	Veil	https://coinmarketcap.com/currencies/veil/	0.0926916981845
509	XTRABYTES	https://coinmarketcap.com/currencies/xtrabytes/	0.00956927689348
510	Selfkey	https://coinmarketcap.com/currencies/selfkey/	0.00143088724019
511	CPChain	https://coinmarketcap.com/currencies/cpchain/	0.0108849767473
512	Bottos	https://coinmarketcap.com/currencies/bottos/	0.0074484455229
513	HashBX	https://coinmarketcap.com/currencies/hashsbx/	0.00983014993998
514	Vexanium	https://coinmarketcap.com/currencies/vexanium/	0.00571603148341
515	Polis	https://coinmarketcap.com/currencies/polis/	0.629046386824
516	TEMCO	https://coinmarketcap.com/currencies/temco/	0.00138416815368
517	Penta	https://coinmarketcap.com/currencies/penta/	0.000190731695184
518	Omnitude	https://coinmarketcap.com/currencies/omnitude/	0.0611168443703
519	Trade Token X	https://coinmarketcap.com/currencies/trade-token-x/	0.046117029779
520	STACS	https://coinmarketcap.com/currencies/stacs/	0.00762160654788
521	YOYOW	https://coinmarketcap.com/currencies/yoyow/	0.0130816113142
522	STPT	https://coinmarketcap.com/currencies/stpt/	0.0134848605746
523	sUSD	https://coinmarketcap.com/currencies/susd/	1.00136972005
524	Universa	https://coinmarketcap.com/currencies/universa/	0.0020869039363
525	Sentinel Prot...	https://coinmarketcap.com/currencies/sentinel-protocol/	0.0126877610276
526	Sentinel	https://coinmarketcap.com/currencies/sentinel/	0.00192159692413
527	SONM	https://coinmarketcap.com/currencies/sonm/	0.0106871615988
528	Traceability ...	https://coinmarketcap.com/currencies/traceability-chain/	0.00576668838723
529	Ondori	https://coinmarketcap.com/currencies/ondori/	0.000100729230458
530	AppCoins	https://coinmarketcap.com/currencies/appcoins/	0.0379865212935
531	GET Protocol	https://coinmarketcap.com/currencies/get-protocol/	0.331828951699
532	Kcash	https://coinmarketcap.com/currencies/kcash/	0.00847599824142
533	Ternio	https://coinmarketcap.com/currencies/ternio/	0.01128209239
534	MediShares	https://coinmarketcap.com/currencies/medishares/	0.00507948962104
535	Gulden	https://coinmarketcap.com/currencies/gulden/	0.00757799228855
536	StableUSD	https://coinmarketcap.com/currencies/stableusd/	1.00175275361
537	Infinitus Token	https://coinmarketcap.com/currencies/infinitus-token/	0.301449703147
538	AirSwap	https://coinmarketcap.com/currencies/airswap/	0.0248679225839
539	WePower	https://coinmarketcap.com/currencies/wepower/	0.00613263991994
540	Wings	https://coinmarketcap.com/currencies/wings/	0.0386819656494
541	Vites	https://coinmarketcap.com/currencies/vites/	0.000100729230458
542	ProChain	https://coinmarketcap.com/currencies/prochain/	0.0748041561635
543	Global Crypto...	https://coinmarketcap.com/currencies/global-cryptocurrency/	0.00292114768327
544	Etherparty	https://coinmarketcap.com/currencies/etherparty/	0.00382962960275
545	Q DAO Governa...	https://coinmarketcap.com/currencies/q-dao-governance-token/	43.4243234528
546	Pirate Chain	https://coinmarketcap.com/currencies/pirate-chain/	0.0306781943025
547	Smartlands	https://coinmarketcap.com/currencies/smartlands/	0.712155659336
548	Substratum	https://coinmarketcap.com/currencies/substratum/	0.00948075826716
549	Mobius	https://coinmarketcap.com/currencies/mobius/	0.00693395702283
550	Credo	https://coinmarketcap.com/currencies/credo/	0.00645378493028
551	Gene Source C...	https://coinmarketcap.com/currencies/gene-source-code-chain/	0.009456406537
552	Lykke	https://coinmarketcap.com/currencies/lykke/	0.0111670549204
553	Dock	https://coinmarketcap.com/currencies/dock/	0.00703530244567
554	SunContract	https://coinmarketcap.com/currencies/suncontract/	0.028818477915
555	OriginTrail	https://coinmarketcap.com/currencies/origintrail/	0.0122687161572
556	Gold Bits Coin	https://coinmarketcap.com/currencies/gold-bits-coin/	0.0331580913255
557	QLC Chain	https://coinmarketcap.com/currencies/qlink/	0.0145508229519
558	Aeron	https://coinmarketcap.com/currencies/aeron/	0.17466122627
559	ColossusXT	https://coinmarketcap.com/currencies/colossusxt/	0.000302187691373
560	Ubiq	https://coinmarketcap.com/currencies/ubiq/	0.0809653197234
561	Phantasma	https://coinmarketcap.com/currencies/phantasma/	0.0582899321125
562	POA Network	https://coinmarketcap.com/currencies/poa-network/	0.0154133182784
563	Nimiq	https://coinmarketcap.com/currencies/nimiq/	0.000752164986476
564	CryptalDash	https://coinmarketcap.com/currencies/cryptaldash/	0.00332459764942
565	Akropolis	https://coinmarketcap.com/currencies/akropolis/	0.00829786255938
566	Rocket Pool	https://coinmarketcap.com/currencies/rocket-pool/	0.334039889708
567	Pandacoin	https://coinmarketcap.com/currencies/pandacoin-pnd/	0.000101150757985
568	Viberate	https://coinmarketcap.com/currencies/viberate/	0.0171124451268
569	STEM CELL COIN	https://coinmarketcap.com/currencies/stem-cell-coin/	0.0102149455003
570	V-ID	https://coinmarketcap.com/currencies/v-id/	0.109970161003
571	Insights Network	https://coinmarketcap.com/currencies/insights-network/	0.022457966774
572	Peerplays	https://coinmarketcap.com/currencies/peerplays-ppy/	0.719154669814
573	LBRY Credits	https://coinmarketcap.com/currencies/library-credit/	0.0120892100066
574	Primecoin	https://coinmarketcap.com/currencies/primecoin/	0.11066681162
575	Trias	https://coinmarketcap.com/currencies/trias/	0.00402738429272
576	MEET.ONE	https://coinmarketcap.com/currencies/meetone/	0.00165757129103
577	PCHAIN	https://coinmarketcap.com/currencies/pchain/	0.00726881882204
578	CanonChain	https://coinmarketcap.com/currencies/cononchain/	0.00568434504811
579	VNT Chain	https://coinmarketcap.com/currencies/vnt-chain/	0.00120300201185
580	AMO Coin	https://coinmarketcap.com/currencies/amo-coin/	0.000392881745239
581	bitUSD	https://coinmarketcap.com/currencies/bitusd/	0.989034735838
582	Blue Whale EX...	https://coinmarketcap.com/currencies/blue-whale-exchange/	0.0776769419376
583	NativeCoin	https://coinmarketcap.com/currencies/native-coin/	0.141797545249
584	DAOstack	https://coinmarketcap.com/currencies/daostack/	0.0743142458776
585	Change	https://coinmarketcap.com/currencies/change/	0.0967069576241
586	Caspian	https://coinmarketcap.com/currencies/caspian/	0.00686199671212
587	Agrello	https://coinmarketcap.com/currencies/agrello-delta/	0.0350888646323
588	POPCHAIN	https://coinmarketcap.com/currencies/popchain/	0.003357677666
589	Skrumble Network	https://coinmarketcap.com/currencies/skrumble-network/	0.00292640336408
590	MVL	https://coinmarketcap.com/currencies/mvl/	0.000389680021921
591	Krios	https://coinmarketcap.com/currencies/krios/	0.0242587404969
592	LinkEye	https://coinmarketcap.com/currencies/linkeye/	0.00494960123993
593	MultiVAC	https://coinmarketcap.com/currencies/multivac/	0.00370618057255
594	DeepOnion	https://coinmarketcap.com/currencies/deeponion/	0.181583267109
595	Machine Xchan...	https://coinmarketcap.com/currencies/machine-xchange-coin/	0.00365461222105
596	OKCash	https://coinmarketcap.com/currencies/okcash/	0.0387550733047
597	Feathercoin	https://coinmarketcap.com/currencies/feathercoin/	0.0115472202182
598	Quanta Utilit...	https://coinmarketcap.com/currencies/quanta-utility-token/	9.82616194565e-05
599	Flowchain	https://coinmarketcap.com/currencies/flowchain/	4.14059507807
600	Apex	https://coinmarketcap.com/currencies/apex/	0.00605898364473
601	eosDAC	https://coinmarketcap.com/currencies/eosdac/	0.00431203784787
602	UNIVERSAL CASH	https://coinmarketcap.com/currencies/ucash/	0.000274264705882
603	Unikoin Gold	https://coinmarketcap.com/currencies/unikoin-gold/	0.0193588700212
604	adToken	https://coinmarketcap.com/currencies/adtoken/	0.00348065705492
605	indaHash	https://coinmarketcap.com/currencies/indahash/	0.00688638687093
606	Neumark	https://coinmarketcap.com/currencies/neumark/	0.0861981893277
607	Xaurum	https://coinmarketcap.com/currencies/xaurum/	0.0314454591595
608	Etheroll	https://coinmarketcap.com/currencies/etheroll/	0.387905223624
609	Edgeless	https://coinmarketcap.com/currencies/edgeless/	0.0231698719886
610	YGGDRASH	https://coinmarketcap.com/currencies/yeed/	0.000494876211993
611	Wowbit	https://coinmarketcap.com/currencies/wowbit/	0.0096987839863
612	Abyss Token	https://coinmarketcap.com/currencies/abyss-token/	0.0117814123507
613	Pascal Coin	https://coinmarketcap.com/currencies/pascal-coin/	0.0957226747311
614	Shift	https://coinmarketcap.com/currencies/shift/	0.200086678347
615	BitDice	https://coinmarketcap.com/currencies/bitdice/	0.0382771075739
616	GameCredits	https://coinmarketcap.com/currencies/gamecredits/	0.0382922830687
617	Winding Tree	https://coinmarketcap.com/currencies/winding-tree/	0.124404788824
618	LiquidApps	https://coinmarketcap.com/currencies/liquid-apps/	0.00967941501896
619	BANKEX	https://coinmarketcap.com/currencies/bankex/	0.0177770064297
620	LEOcoin	https://coinmarketcap.com/currencies/leocoin/	0.0217056890703
621	IHT Real Esta...	https://coinmarketcap.com/currencies/iht-real-estate-protocol/	0.00355296961368
622	Stronghold Token	https://coinmarketcap.com/currencies/stronghold-token/	0.000776487710273
623	Esportbits	https://coinmarketcap.com/currencies/esportbits/	0.130614036505
624	ALQO	https://coinmarketcap.com/currencies/alqo/	0.0454288829364
625	GoldCoin	https://coinmarketcap.com/currencies/goldcoin/	0.0622125334915
626	Mooncoin	https://coinmarketcap.com/currencies/mooncoin/	1.13901130937e-05
627	Hashgard	https://coinmarketcap.com/currencies/hashgard/	4.53385348742e-05
628	Quark	https://coinmarketcap.com/currencies/quark/	0.00986982019729
629	ZClassic	https://coinmarketcap.com/currencies/zclassic/	0.348370477109
630	Starta	https://coinmarketcap.com/currencies/starta/	0.510007495467
631	Qitmeer	https://coinmarketcap.com/currencies/qitmeer/	0.00654739928751
632	BaaSid	https://coinmarketcap.com/currencies/baasid/	0.000604375382746
633	BitNewChain	https://coinmarketcap.com/currencies/bitnewchain/	0.014075212879
634	Constant	https://coinmarketcap.com/currencies/constant/	49.836768176
635	ECC	https://coinmarketcap.com/currencies/eccoin/	0.000100712450993
636	VINchain	https://coinmarketcap.com/currencies/vinchain/	0.00426203024937
637	ChatCoin	https://coinmarketcap.com/currencies/chatcoin/	0.00362379979969
638	Adshares	https://coinmarketcap.com/currencies/adshares/	0.070545686933
639	Enecuum	https://coinmarketcap.com/currencies/enecuum/	0.0818595379963
640	CoinUs	https://coinmarketcap.com/currencies/coinus/	0.00719862730675
641	BOLT	https://coinmarketcap.com/currencies/bolt/	0.00592252091649
642	Loopring [NEO]	https://coinmarketcap.com/currencies/loopring-neo/	0.021468599013
643	MobileGo	https://coinmarketcap.com/currencies/mobilego/	0.0243709708432
644	Footballcoin	https://coinmarketcap.com/currencies/footballcoin/	0.00650179588381
645	ugChain	https://coinmarketcap.com/currencies/ugchain/	0.00426640375373
646	Ambrosus	https://coinmarketcap.com/currencies/amber/	0.0167325678514
647	LoyalCoin	https://coinmarketcap.com/currencies/loyalcoin/	0.00045002920786
648	Ecobit	https://coinmarketcap.com/currencies/ecobit/	0.00538328315978
649	Sentivate	https://coinmarketcap.com/currencies/sentivate/	0.00105510256776
650	Ultra	https://coinmarketcap.com/currencies/ultra/	0.0300431730605
651	I/O Coin	https://coinmarketcap.com/currencies/iocoin/	0.134473522661
652	EncrypGen	https://coinmarketcap.com/currencies/encrypgen/	0.0351399572464
653	Observer	https://coinmarketcap.com/currencies/observer/	0.00175739491708
654	XinFin Network	https://coinmarketcap.com/currencies/xinfin-network/	0.000606682243038
655	S4FE	https://coinmarketcap.com/currencies/s4fe/	0.00879183164727
656	Remme	https://coinmarketcap.com/currencies/remme/	0.00351898220538
657	Sessia	https://coinmarketcap.com/currencies/sessia/	0.398070804979
658	Nexty	https://coinmarketcap.com/currencies/nexty/	1.53137238323e-05
659	SDChain	https://coinmarketcap.com/currencies/sdchain/	0.00153047907206
660	YEE	https://coinmarketcap.com/currencies/yee/	0.00168139094315
661	Lunyr	https://coinmarketcap.com/currencies/lunyr/	0.997331676012
662	NeoWorld Cash	https://coinmarketcap.com/currencies/neoworld-cash/	0.000111113471603
663	SafeCoin	https://coinmarketcap.com/currencies/safecoin/	0.0815906766707
664	Airbloc	https://coinmarketcap.com/currencies/airbloc/	0.00896590263111
665	MintCoin	https://coinmarketcap.com/currencies/mintcoin/	8.95811181658e-05
666	Bitcoin Confi...	https://coinmarketcap.com/currencies/bitcoin-confidential/	0.000302187691373
667	BridgeCoin	https://coinmarketcap.com/currencies/bridgecoin/	0.0819174995463
668	CoinPoker	https://coinmarketcap.com/currencies/coinpoker/	0.00719852213599
669	Diamond	https://coinmarketcap.com/currencies/diamond/	0.661839660518
670	Global Curren...	https://coinmarketcap.com/currencies/global-currency-reserve/	0.0204480337829
671	Maecenas	https://coinmarketcap.com/currencies/maecenas/	0.0368380612072
672	MIR COIN	https://coinmarketcap.com/currencies/mir-coin/	0.00346304446483
673	Ubex	https://coinmarketcap.com/currencies/ubex/	0.000688471558737
675	PIBBLE	https://coinmarketcap.com/currencies/pibble/	0.000251825259715
676	Lition	https://coinmarketcap.com/currencies/lition/	0.0824126096598
677	X-CASH	https://coinmarketcap.com/currencies/x-cash/	4.85724473782e-05
678	Cryptopay	https://coinmarketcap.com/currencies/cryptopay/	0.0304310848704
679	Fatcoin	https://coinmarketcap.com/currencies/fatcoin/	0.0153585716022
680	Origin Sport	https://coinmarketcap.com/currencies/origin-sport/	0.0112675462944
681	0Chain	https://coinmarketcap.com/currencies/0chain/	0.0509663628504
682	Zen Protocol	https://coinmarketcap.com/currencies/zen-protocol/	0.0900971674202
683	BitBay	https://coinmarketcap.com/currencies/bitbay/	0.00201458460915
684	TE-FOOD	https://coinmarketcap.com/currencies/te-food/	0.00393297836631
685	Phore	https://coinmarketcap.com/currencies/phore/	0.109348421982
686	Flixxo	https://coinmarketcap.com/currencies/flixxo/	0.0239490676968
687	Grid+	https://coinmarketcap.com/currencies/grid/	0.0513173167774
688	RedFOX Labs	https://coinmarketcap.com/currencies/redfox-labs/	0.0204520382653
689	Ink	https://coinmarketcap.com/currencies/ink/	0.00431690838237
690	MARK.SPACE	https://coinmarketcap.com/currencies/mark-space/	0.00258066871213
691	MassGrid	https://coinmarketcap.com/currencies/massgrid/	0.0267424523441
692	Ulord	https://coinmarketcap.com/currencies/ulord/	0.0173051313185
693	PolySwarm	https://coinmarketcap.com/currencies/polyswarm/	0.00128240574185
694	Merculet	https://coinmarketcap.com/currencies/merculet/	0.000818602639307
695	SpankChain	https://coinmarketcap.com/currencies/spankchain/	0.00657774150474
696	aXpire	https://coinmarketcap.com/currencies/axpire/	0.0069468488585
697	Chromia	https://coinmarketcap.com/currencies/chromia/	0.0392543140069
698	FansTime	https://coinmarketcap.com/currencies/fanstime/	0.000686623581217
699	Bloom	https://coinmarketcap.com/currencies/bloomtoken/	0.0364639814257
700	ATN	https://coinmarketcap.com/currencies/atn/	0.0231677230053
701	Noku	https://coinmarketcap.com/currencies/noku/	0.0820502943762
702	Insureum	https://coinmarketcap.com/currencies/insureum/	0.0090588671248
703	Beetle Coin	https://coinmarketcap.com/currencies/beetle-coin/	0.00965613003776
704	Eterbase Coin	https://coinmarketcap.com/currencies/eterbase-coin/	0.00195571615001
705	DECENT	https://coinmarketcap.com/currencies/decent/	0.0372837408768
706	SelfSell	https://coinmarketcap.com/currencies/selfsell/	0.00489209406504
707	nOS	https://coinmarketcap.com/currencies/nos/	0.0184172329117
708	AIDUS TOKEN	https://coinmarketcap.com/currencies/aidus-token/	0.0094315089518
709	Ampleforth	https://coinmarketcap.com/currencies/ampleforth/	0.441233382686
710	ATC Coin	https://coinmarketcap.com/currencies/atc-coin/	0.00523779791833
711	DaTa eXchange	https://coinmarketcap.com/currencies/data-exchange/	0.0243122643029
712	Ormeus Coin	https://coinmarketcap.com/currencies/ormeus-coin/	0.0520195216139
713	Coinsuper Eco...	https://coinmarketcap.com/currencies/coinsuper-ecosystem-network/	0.00461817845602
714	CloakCoin	https://coinmarketcap.com/currencies/cloakcoin/	0.348142710712
715	Waves Communi...	https://coinmarketcap.com/currencies/waves-community-token/	0.185758532007
716	Medicalchain	https://coinmarketcap.com/currencies/medical-chain/	0.00634942248856
717	Kambria	https://coinmarketcap.com/currencies/kambria/	0.00149644409971
718	SINOVATE	https://coinmarketcap.com/currencies/sinovate/	0.00285739760345
719	Paragon	https://coinmarketcap.com/currencies/paragon/	0.0282860218457
720	Hxro	https://coinmarketcap.com/currencies/hxro/	0.0314009125198
721	Rubycoin	https://coinmarketcap.com/currencies/rubycoin/	0.0667854720128
722	Streamit Coin	https://coinmarketcap.com/currencies/streamit-coin/	1.79735247961
723	Asian Fintech	https://coinmarketcap.com/currencies/asian-fintech/	0.00720158678123
724	Moneytoken	https://coinmarketcap.com/currencies/moneytoken/	0.000190150901384
725	AI Doctor	https://coinmarketcap.com/currencies/aidoc/	0.00403457668746
726	Stealth	https://coinmarketcap.com/currencies/stealth/	0.0533864921426
727	W Green Pay	https://coinmarketcap.com/currencies/w-green-pay/	0.194105817179
728	EOSDT	https://coinmarketcap.com/currencies/eosdt/	0.98363280383
729	Liquidity Net...	https://coinmarketcap.com/currencies/liquidity-network/	0.0406481597733
730	NOIA Network	https://coinmarketcap.com/currencies/noia-network/	0.0363712841204
731	BOMB	https://coinmarketcap.com/currencies/bomb/	1.82673349976
732	PetroDollar	https://coinmarketcap.com/currencies/petrodollar/	0.027192361768
733	Dignity	https://coinmarketcap.com/currencies/dignity/	0.00332178287767
734	ERC20	https://coinmarketcap.com/currencies/erc20/	0.0347059416959
735	FairCoin	https://coinmarketcap.com/currencies/faircoin/	0.0325377733411
736	NeuroChain	https://coinmarketcap.com/currencies/neurochain/	0.00408876437875
737	Brickblock	https://coinmarketcap.com/currencies/brickblock/	0.0229004747822
738	eXPerience Chain	https://coinmarketcap.com/currencies/experience-chain/	1.87929616852e-05
739	DAEX	https://coinmarketcap.com/currencies/daex/	0.00482008520694
740	Unibright	https://coinmarketcap.com/currencies/unibright/	0.0122362904459
741	Qwertycoin	https://coinmarketcap.com/currencies/qwertycoin/	1.71239691778e-05
742	Primalbase Token	https://coinmarketcap.com/currencies/primalbase/	1364.40205407
743	BitGreen	https://coinmarketcap.com/currencies/bitgreen/	0.173370574525
744	Opacity	https://coinmarketcap.com/currencies/opacity/	0.0134650342048
745	TurtleCoin	https://coinmarketcap.com/currencies/turtlecoin/	3.18976301798e-05
746	COTI	https://coinmarketcap.com/currencies/coti/	0.0228537473026
747	EBCoin	https://coinmarketcap.com/currencies/ebcoin/	0.000368680028825
748	LikeCoin	https://coinmarketcap.com/currencies/likecoin/	0.00355925365596
749	Spectre.ai Ut...	https://coinmarketcap.com/currencies/spectre-utility/	0.0686640840162
750	Nasdacoin	https://coinmarketcap.com/currencies/nasdacoin/	0.081641202959
751	SafeInsure	https://coinmarketcap.com/currencies/safeinsure/	0.474562047399
752	Snetwork	https://coinmarketcap.com/currencies/snetwork/	0.0106725923096
753	Datum	https://coinmarketcap.com/currencies/datum/	0.00166381957019
754	Niobium Coin	https://coinmarketcap.com/currencies/niobium-coin/	0.03380171317
755	VeriCoin	https://coinmarketcap.com/currencies/vericoin/	0.0510660836658
756	CargoX	https://coinmarketcap.com/currencies/cargox/	0.0105434280091
757	carVertical	https://coinmarketcap.com/currencies/carvertical/	0.000213670913261
758	BOSAGORA	https://coinmarketcap.com/currencies/bosagora/	0.00997559722205
759	HTMLCOIN	https://coinmarketcap.com/currencies/html-coin/	3.05528790479e-05
760	Golfcoin	https://coinmarketcap.com/currencies/golfcoin/	4.58529770963e-05
761	Rate3	https://coinmarketcap.com/currencies/rate3/	0.00182000764833
762	Callisto Network	https://coinmarketcap.com/currencies/callisto-network/	0.000814867024747
763	Effect.AI	https://coinmarketcap.com/currencies/effect-ai/	0.00637765004037
764	COVA	https://coinmarketcap.com/currencies/cova/	0.000640223406575
765	ALIS	https://coinmarketcap.com/currencies/alis/	0.0402916921831
766	1SG	https://coinmarketcap.com/currencies/1sg/	0.723409659944
767	Skychain	https://coinmarketcap.com/currencies/skychain/	0.211430654731
768	EXRNchain	https://coinmarketcap.com/currencies/exrnchain/	1.70740462386e-05
769	BlockStamp	https://coinmarketcap.com/currencies/blockstamp/	0.0777065086978
770	Fountain	https://coinmarketcap.com/currencies/fountain/	0.0240098229472
771	Mcashchain	https://coinmarketcap.com/currencies/mcashchain/	0.014901786843
772	Radium	https://coinmarketcap.com/currencies/radium/	0.409553477493
773	AMLT	https://coinmarketcap.com/currencies/amlt/	0.00651499117423
774	NAGA	https://coinmarketcap.com/currencies/naga/	0.0217411060438
775	WeShow Token	https://coinmarketcap.com/currencies/weshow-token/	0.00970798728856
776	PotCoin	https://coinmarketcap.com/currencies/potcoin/	0.0069491591185
777	Block-Chain.com	https://coinmarketcap.com/currencies/block-chain-com/	0.00747443267752
778	Blocktrade Token	https://coinmarketcap.com/currencies/blocktrade-token/	0.0277291079365
779	Myriad	https://coinmarketcap.com/currencies/myriad/	0.00090643295438
780	WeTrust	https://coinmarketcap.com/currencies/trust/	0.0166896299194
781	CanYaCoin	https://coinmarketcap.com/currencies/canyacoin/	0.0166409907944
782	VegaWallet Token	https://coinmarketcap.com/currencies/vegawallet-token/	0.118247877439
783	Peculium	https://coinmarketcap.com/currencies/peculium/	0.000752237820725
784	Spendcoin	https://coinmarketcap.com/currencies/spendcoin/	0.00312238725778
785	Coineal Token	https://coinmarketcap.com/currencies/coineal-token/	0.00481076973829
786	KickToken	https://coinmarketcap.com/currencies/kick-token/	0.000912696698685
787	Eden	https://coinmarketcap.com/currencies/eden/	0.00249111424101
788	BitTube	https://coinmarketcap.com/currencies/bit-tube/	0.0101711734599
789	HashCoin	https://coinmarketcap.com/currencies/hashcoin/	0.000114665125678
790	Bitcoin Atom	https://coinmarketcap.com/currencies/bitcoin-atom/	0.0797320065757
791	Optimal Shelf...	https://coinmarketcap.com/currencies/optimal-shelf-availability-token/	0.00105465288112
792	Lamden	https://coinmarketcap.com/currencies/lamden/	0.0102866327166
793	PlayCoin [ERC20]	https://coinmarketcap.com/currencies/playcoin-erc20/	0.00807950579904
794	EchoLink	https://coinmarketcap.com/currencies/echolink/	0.00291953777319
795	Colu Local Ne...	https://coinmarketcap.com/currencies/colu-local-network/	0.0150260218234
796	BABB	https://coinmarketcap.com/currencies/babb/	5.62949791438e-05
797	STK	https://coinmarketcap.com/currencies/stk/	0.00422888966215
798	Kleros	https://coinmarketcap.com/currencies/kleros/	0.00641413148386
799	PAC Global	https://coinmarketcap.com/currencies/pac-global/	0.000189942048082
800	Zebi	https://coinmarketcap.com/currencies/zebi/	0.00340160559349
801	Verasity	https://coinmarketcap.com/currencies/verasity/	0.000573511481261
802	NuShares	https://coinmarketcap.com/currencies/nushares/	0.000516698060731
803	Kryll	https://coinmarketcap.com/currencies/kryll/	0.0590964832224
804	Internet Node...	https://coinmarketcap.com/currencies/internet-node-token/	0.0269493856307
805	Covesting	https://coinmarketcap.com/currencies/covesting/	0.079000423553
806	SolarCoin	https://coinmarketcap.com/currencies/solarcoin/	0.0254367961277
807	Education Eco...	https://coinmarketcap.com/currencies/education-ecosystem/	0.00649353999257
808	FuzeX	https://coinmarketcap.com/currencies/fuzex/	0.0017119463743
809	Hiveterminal ...	https://coinmarketcap.com/currencies/hiveterminal-token/	0.00339974990034
810	QChi	https://coinmarketcap.com/currencies/qchi/	0.0430548913634
811	THORChain	https://coinmarketcap.com/currencies/thorchain/	0.0161928749477
812	CVCoin	https://coinmarketcap.com/currencies/cvcoin/	0.11269805601
813	Dimecoin	https://coinmarketcap.com/currencies/dimecoin/	2.5611918633e-06
814	Fast Access B...	https://coinmarketcap.com/currencies/fast-access-blockchain/	0.0485838124039
815	EveryCoin	https://coinmarketcap.com/currencies/everycoin/	0.000146615428383
816	Flash	https://coinmarketcap.com/currencies/flash/	0.00151252705651
817	Switcheo	https://coinmarketcap.com/currencies/switcheo/	0.00259551233353
818	Typerium	https://coinmarketcap.com/currencies/typerium/	0.000831588759706
819	SureRemit	https://coinmarketcap.com/currencies/sureremit/	0.00268819277782
820	DACSEE	https://coinmarketcap.com/currencies/dacsee/	0.00177935933367
821	Safe Haven	https://coinmarketcap.com/currencies/safe-haven/	0.000446756954629
822	HiCoin	https://coinmarketcap.com/currencies/hicoin/	0.000302193076463
823	Kuai Token	https://coinmarketcap.com/currencies/kuai-token/	0.139364332227
824	Crown	https://coinmarketcap.com/currencies/crown/	0.0575391156552
825	GridCoin	https://coinmarketcap.com/currencies/gridcoin/	0.00312266179012
826	SpaceChain	https://coinmarketcap.com/currencies/spacechain/	0.00255710850397
827	MidasProtocol	https://coinmarketcap.com/currencies/midasprotocol/	0.00419606162426
828	Naka Bodhi Token	https://coinmarketcap.com/currencies/naka-bodhi-token/	0.0212071088004
829	Tolar	https://coinmarketcap.com/currencies/tolar/	0.00517342553722
830	ShipChain	https://coinmarketcap.com/currencies/shipchain/	0.00485687520922
831	FintruX Network	https://coinmarketcap.com/currencies/fintrux-network/	0.0133519873871
832	HempCoin	https://coinmarketcap.com/currencies/hempcoin/	0.00502727720561
833	FREE Coin	https://coinmarketcap.com/currencies/free-coin/	1.4559705004e-07
834	FNKOS	https://coinmarketcap.com/currencies/fnkos/	0.00815433485481
835	IQeon	https://coinmarketcap.com/currencies/iqeon/	0.452094581838
836	Quasarcoin	https://coinmarketcap.com/currencies/quasarcoin/	0.00746316054571
837	PTON	https://coinmarketcap.com/currencies/pton/	0.000112729625455
838	CrypticCoin	https://coinmarketcap.com/currencies/crypticcoin/	0.000491085668334
839	Zeepin	https://coinmarketcap.com/currencies/zeepin/	0.00249762525518
840	SPINDLE	https://coinmarketcap.com/currencies/spindle/	0.000387877132677
841	Zilla	https://coinmarketcap.com/currencies/zilla/	0.0207434369699
842	Semux	https://coinmarketcap.com/currencies/semux/	0.106168092388
843	TrueFlip	https://coinmarketcap.com/currencies/trueflip/	0.197065267472
844	Tidex Token	https://coinmarketcap.com/currencies/tidex-token/	0.129233098177
845	Matrexcoin	https://coinmarketcap.com/currencies/matrexcoin/	0.0711685460133
846	AICHAIN	https://coinmarketcap.com/currencies/aichain/	0.00228090148447
847	Orbitcoin	https://coinmarketcap.com/currencies/orbitcoin/	0.376137291676
848	Zenswap Netwo...	https://coinmarketcap.com/currencies/zenswap-network-token/	0.000100729230458
849	PARETO Rewards	https://coinmarketcap.com/currencies/pareto-rewards/	0.00256547677264
850	qiibee	https://coinmarketcap.com/currencies/qiibee/	0.00269852493975
851	CEEK VR	https://coinmarketcap.com/currencies/ceek-vr/	0.00237373582565
852	IONChain	https://coinmarketcap.com/currencies/ionchain/	0.00969837229108
853	Cloudbric	https://coinmarketcap.com/currencies/cloudbric/	0.00275869102611
854	CashBet Coin	https://coinmarketcap.com/currencies/cashbet-coin/	0.00722853745766
855	Pigeoncoin	https://coinmarketcap.com/currencies/pigeoncoin/	0.000336816960563
856	Digital Asset...	https://coinmarketcap.com/currencies/digital-asset-guarantee-token/	0.0503741169928
857	Novacoin	https://coinmarketcap.com/currencies/novacoin/	0.494470515814
858	Consensus	https://coinmarketcap.com/currencies/consensus/	0.000709424576067
859	ADAMANT Messe...	https://coinmarketcap.com/currencies/adamant-messenger/	0.0139428063724
860	Hacken	https://coinmarketcap.com/currencies/hacken/	0.197700560673
861	VeriSafe	https://coinmarketcap.com/currencies/verisafe/	0.000105104310022
862	RevolutionVR	https://coinmarketcap.com/currencies/revolutionvr/	0.00543947537634
863	Rapids	https://coinmarketcap.com/currencies/rapids/	0.000104723599335
864	Humaniq	https://coinmarketcap.com/currencies/humaniq/	0.00601148008319
865	Bismuth	https://coinmarketcap.com/currencies/bismuth/	0.0808818977323
866	smARTOFGIVING	https://coinmarketcap.com/currencies/smartofgiving/	0.0151093845687
867	Cryptocean	https://coinmarketcap.com/currencies/cryptocean/	0.170108951702
868	Bitcoin Private	https://coinmarketcap.com/currencies/bitcoin-private/	0.230595272266
869	Sense	https://coinmarketcap.com/currencies/sense/	0.00184976946426
870	Chronobank	https://coinmarketcap.com/currencies/chronobank/	1.53028845927
871	Friendz	https://coinmarketcap.com/currencies/friends/	0.00212649030304
872	DreamTeam Token	https://coinmarketcap.com/currencies/dreamteam-token/	0.0300021329788
873	Presearch	https://coinmarketcap.com/currencies/presearch/	0.00708147561215
874	Global Awards...	https://coinmarketcap.com/currencies/global-awards-token/	0.0015667717625
875	Internxt	https://coinmarketcap.com/currencies/internxt/	1.69731475257
876	Bitcoin Interest	https://coinmarketcap.com/currencies/bitcoin-interest/	0.0582417257716
877	LUXCoin	https://coinmarketcap.com/currencies/luxcoin/	0.167365390357
878	Max Property ...	https://coinmarketcap.com/currencies/max-property-group/	0.009057556708
879	Golos	https://coinmarketcap.com/currencies/golos/	0.00604386152926
880	Vezt	https://coinmarketcap.com/currencies/vezt/	0.0123134047713
881	Haven Protocol	https://coinmarketcap.com/currencies/haven-protocol/	0.134344959235
882	IG Gold	https://coinmarketcap.com/currencies/ig-gold/	0.000108752393923
883	Experience Po...	https://coinmarketcap.com/currencies/experience-points/	3.63593269616e-06
884	Pundi X NEM	https://coinmarketcap.com/currencies/pundi-x-nem/	0.000429834150138
885	RoBET	https://coinmarketcap.com/currencies/robet/	1.30338280377
886	Plair	https://coinmarketcap.com/currencies/plair/	5.17692136837e-05
887	Spiking	https://coinmarketcap.com/currencies/spiking/	0.00231675459983
888	Uquid Coin	https://coinmarketcap.com/currencies/uquid-coin/	0.102287602396
889	CryptoPing	https://coinmarketcap.com/currencies/cryptoping/	0.102655199177
890	Vanta Network	https://coinmarketcap.com/currencies/vanta-network/	0.000362246133972
891	PAYCENT	https://coinmarketcap.com/currencies/paycent/	0.0331927268383
892	Paypex	https://coinmarketcap.com/currencies/paypex/	0.0147671296997
893	Nework	https://coinmarketcap.com/currencies/nework/	0.00681189632194
894	Fortuna	https://coinmarketcap.com/currencies/fortuna/	0.00209614028137
895	ICE ROCK MINING	https://coinmarketcap.com/currencies/ice-rock-mining/	0.0638590275243
896	SophiaTX	https://coinmarketcap.com/currencies/sophiatx/	0.00303920555041
897	GMB	https://coinmarketcap.com/currencies/gmb/	0.00192885480536
898	DATx	https://coinmarketcap.com/currencies/datx/	0.0007160455766
899	Mysterium	https://coinmarketcap.com/currencies/mysterium/	0.0415855945162
900	Cardstack	https://coinmarketcap.com/currencies/cardstack/	0.000415812881144
901	Bean Cash	https://coinmarketcap.com/currencies/bean-cash/	0.000303269629802
902	e-Gulden	https://coinmarketcap.com/currencies/e-gulden/	0.057416684528
903	Sealchain	https://coinmarketcap.com/currencies/sealchain/	0.0217800677859
904	PWR Coin	https://coinmarketcap.com/currencies/powercoin/	0.000100731025488
905	Curecoin	https://coinmarketcap.com/currencies/curecoin/	0.039652103293
906	Matryx	https://coinmarketcap.com/currencies/matryx/	0.0411986921367
907	Acute Angle C...	https://coinmarketcap.com/currencies/acute-angle-cloud/	0.00382752913913
908	NewYorkCoin	https://coinmarketcap.com/currencies/newyorkcoin/	7.12001645451e-06
909	MonetaryUnit	https://coinmarketcap.com/currencies/monetaryunit/	0.00563418735091
910	GAMB	https://coinmarketcap.com/currencies/gamb/	0.000283180828256
911	Next.exchange	https://coinmarketcap.com/currencies/next-exchange/	0.2430618199
912	ZPER	https://coinmarketcap.com/currencies/zper/	0.000721723583355
913	BitCrystals	https://coinmarketcap.com/currencies/bitcrystals/	0.0411924653082
914	Swisscoin	https://coinmarketcap.com/currencies/swisscoin/	0.000102322747015
915	Cappasity	https://coinmarketcap.com/currencies/cappasity/	0.00174406902166
916	Aryacoin	https://coinmarketcap.com/currencies/aryacoin/	0.005048100516
917	Cashbery Coin	https://coinmarketcap.com/currencies/cashbery-coin/	0.0139039631844
918	Oxycoin	https://coinmarketcap.com/currencies/oxycoin/	0.00100404237253
919	Conceal	https://coinmarketcap.com/currencies/conceal/	0.197654718116
920	XEL	https://coinmarketcap.com/currencies/xel/	0.0101139561275
921	Neurotoken	https://coinmarketcap.com/currencies/neurotoken/	0.0115897912348
922	Lisk Machine ...	https://coinmarketcap.com/currencies/lisk-machine-learning/	0.00760532423399
923	Unification	https://coinmarketcap.com/currencies/unification/	0.0233284995157
924	Nuggets	https://coinmarketcap.com/currencies/nuggets/	0.000525013694173
925	Bounty0x	https://coinmarketcap.com/currencies/bounty0x/	0.00388157258805
926	Pluton	https://coinmarketcap.com/currencies/pluton/	1.06113493905
927	ONOToken	https://coinmarketcap.com/currencies/onotoken/	5.51684316674e-05
928	42-coin	https://coinmarketcap.com/currencies/42-coin/	20965.0201581
929	Storeum	https://coinmarketcap.com/currencies/storeum/	0.00694054462913
930	Proxeus	https://coinmarketcap.com/currencies/proxeus/	0.00427110438716
931	Ifoods Chain	https://coinmarketcap.com/currencies/ifoods-chain/	0.000347065539918
932	Blue Protocol	https://coinmarketcap.com/currencies/ethereum-blue/	0.0236849482986
933	NuBits	https://coinmarketcap.com/currencies/nubits/	0.078973727741
934	Xriba	https://coinmarketcap.com/currencies/xriba/	0.00883519769731
935	SIBCoin	https://coinmarketcap.com/currencies/sibcoin/	0.0483430491022
936	Graft	https://coinmarketcap.com/currencies/graft/	0.00147002497379
937	Online	https://coinmarketcap.com/currencies/online/	0.000980574382218
938	Zeusshield	https://coinmarketcap.com/currencies/zeusshield/	0.000689132205721
939	BiblePay	https://coinmarketcap.com/currencies/biblepay/	0.000481599371213
940	Raven Protocol	https://coinmarketcap.com/currencies/raven-protocol/	0.000460923348447
941	WomenCoin	https://coinmarketcap.com/currencies/women/	1.74234682387e-05
942	UpToken	https://coinmarketcap.com/currencies/uptoken/	0.00574156613609
943	Bitcoin Plus	https://coinmarketcap.com/currencies/bitcoin-plus/	6.51857037122
944	HorusPay	https://coinmarketcap.com/currencies/horuspay/	0.000960434199055
945	TRAXIA	https://coinmarketcap.com/currencies/traxia/	0.00166744310798
946	ATLANT	https://coinmarketcap.com/currencies/atlant/	0.015395312989
947	WinStars.live	https://coinmarketcap.com/currencies/winstars-live/	0.0500535802576
948	LIFE	https://coinmarketcap.com/currencies/life/	3.50545098981e-05
949	Omni	https://coinmarketcap.com/currencies/omni/	1.45254196434
950	Bezop	https://coinmarketcap.com/currencies/bezop/	0.0146298044701
951	DecentBet	https://coinmarketcap.com/currencies/decent-bet/	0.0042992074356
952	Prometeus	https://coinmarketcap.com/currencies/prometeus/	0.210524818862
953	WOLLO	https://coinmarketcap.com/currencies/wollo/	0.0186045055765
954	0xBitcoin	https://coinmarketcap.com/currencies/0xbtc/	0.158854304399
955	X8X Token	https://coinmarketcap.com/currencies/x8x-token/	0.0101440406933
956	Coinvest	https://coinmarketcap.com/currencies/coinvest/	0.0673096630989
957	RED	https://coinmarketcap.com/currencies/red/	0.00609033050595
958	Stox	https://coinmarketcap.com/currencies/stox/	0.0147963381604
959	AC3	https://coinmarketcap.com/currencies/ac3/	0.0016077849943
960	Labh Coin	https://coinmarketcap.com/currencies/labh-coin/	5.79260308844e-05
961	Espers	https://coinmarketcap.com/currencies/espers/	3.38820032429e-05
962	DABANKING	https://coinmarketcap.com/currencies/dabanking/	0.551168647946
963	ESBC	https://coinmarketcap.com/currencies/esbc/	0.0437333862033
964	Vodi X	https://coinmarketcap.com/currencies/vodi-x/	0.00219188438478
965	Trittium	https://coinmarketcap.com/currencies/trittium/	0.00592771442499
966	RightMesh	https://coinmarketcap.com/currencies/rightmesh/	0.0107064013504
967	EvenCoin	https://coinmarketcap.com/currencies/evencoin/	0.0252408958916
968	Trinity Netwo...	https://coinmarketcap.com/currencies/trinity-network-credit/	0.00226377054416
969	TouchCon	https://coinmarketcap.com/currencies/touchcon/	0.00323072002811
970	COS	https://coinmarketcap.com/currencies/cos/	0.0240887116711
971	VouchForMe	https://coinmarketcap.com/currencies/insurepal/	0.00325197495336
972	Digital Insur...	https://coinmarketcap.com/currencies/digital-insurance-token/	0.00329938904756
973	LocalCoinSwap	https://coinmarketcap.com/currencies/local-coin-swap/	0.0137999045727
974	Sentinel Chain	https://coinmarketcap.com/currencies/sentinel-chain/	0.00372252472937
975	CoinFi	https://coinmarketcap.com/currencies/coinfi/	0.00372748950168
976	WebDollar	https://coinmarketcap.com/currencies/webdollar/	0.000116901019587
977	ELA Coin	https://coinmarketcap.com/currencies/ela-coin/	0.00408668806872
978	Storiqa	https://coinmarketcap.com/currencies/storiqa/	6.68459036628e-05
979	iEthereum	https://coinmarketcap.com/currencies/iethereum/	0.0405539556814
980	Upfiring	https://coinmarketcap.com/currencies/upfiring/	0.0334751209825
981	MESG	https://coinmarketcap.com/currencies/mesg/	0.0290005593742
982	INMAX	https://coinmarketcap.com/currencies/inmax/	0.199554712249
983	Qbao	https://coinmarketcap.com/currencies/qbao/	0.0108282548846
984	EnergiToken	https://coinmarketcap.com/currencies/energitoken/	0.000380602538724
985	DomRaider	https://coinmarketcap.com/currencies/domraider/	0.00118694480646
986	Terracoin	https://coinmarketcap.com/currencies/terracoin/	0.0302894538419
987	Netrum	https://coinmarketcap.com/currencies/netrum/	0.304734724866
988	Vipstar Coin	https://coinmarketcap.com/currencies/vipstar-coin/	1.95758951078e-05
989	HOLD	https://coinmarketcap.com/currencies/hold/	0.000973455874906
990	GoldMint	https://coinmarketcap.com/currencies/goldmint/	0.354928609869
991	DPRating	https://coinmarketcap.com/currencies/dprating/	0.000261588625644
992	Datawallet	https://coinmarketcap.com/currencies/datawallet/	0.00172597617269
993	Banca	https://coinmarketcap.com/currencies/banca/	3.74378441784e-05
994	Aventus	https://coinmarketcap.com/currencies/aventus/	0.111770032505
995	FarmaTrust	https://coinmarketcap.com/currencies/farmatrust/	0.00109796472316
996	NANJCOIN	https://coinmarketcap.com/currencies/nanjcoin/	3.38129066268e-05
997	Business Cred...	https://coinmarketcap.com/currencies/business-credit-alliance-chain/	0.00116940293172
998	Electrify.Asia	https://coinmarketcap.com/currencies/electrifyasia/	0.00121983810276
999	Thrive Token	https://coinmarketcap.com/currencies/thrive-token/	0.00624521228838
1000	Nebula AI	https://coinmarketcap.com/currencies/nebula-ai/	0.000511100549179
1001	Essentia	https://coinmarketcap.com/currencies/essentia/	0.000759079379531
1002	Dynamic	https://coinmarketcap.com/currencies/dynamic/	0.0430648374573
1003	Open Platform	https://coinmarketcap.com/currencies/open-platform/	0.000885576085638
1004	DIMCOIN	https://coinmarketcap.com/currencies/dimcoin/	0.00030256694116
1005	BitBall	https://coinmarketcap.com/currencies/bitball/	0.00797790367123
1006	Atomic Wallet...	https://coinmarketcap.com/currencies/atomic-wallet-coin/	0.101398142061
1007	Pinkcoin	https://coinmarketcap.com/currencies/pinkcoin/	0.00151069444437
1008	ION	https://coinmarketcap.com/currencies/ion/	0.041106070714
1009	HEAT	https://coinmarketcap.com/currencies/heat-ledger/	0.0147064676468
1010	VisionX	https://coinmarketcap.com/currencies/visionx/	0.000171202803884
1011	TigerCash	https://coinmarketcap.com/currencies/tigercash/	0.0241828199649
1012	FortKnoxster	https://coinmarketcap.com/currencies/fortknoxster/	0.00410934325316
1013	DNotes	https://coinmarketcap.com/currencies/dnotes/	0.00453232402353
1014	Bittwatt	https://coinmarketcap.com/currencies/bittwatt/	0.00197688847111
1015	Blockchain Ce...	https://coinmarketcap.com/currencies/blockchain-certified-data-token/	0.0187963169402
1016	FLIP	https://coinmarketcap.com/currencies/flip/	0.0107843695378
1017	Pirl	https://coinmarketcap.com/currencies/pirl/	0.0112934492491
1018	Ethbits	https://coinmarketcap.com/currencies/ethbits/	0.362625229648
1019	Patientory	https://coinmarketcap.com/currencies/patientory/	0.00840583190782
1020	Alphacat	https://coinmarketcap.com/currencies/alphacat/	0.000210631727895
1021	Halo Platform	https://coinmarketcap.com/currencies/halo-platform/	0.000121014624303
1022	Vision Indust...	https://coinmarketcap.com/currencies/vision-industry-token/	0.000201458460915
1023	Blockparty (B...	https://coinmarketcap.com/currencies/blockparty-boxx-token/	0.0179655079724
1024	Paytomat	https://coinmarketcap.com/currencies/paytomat/	0.00290028503168
1025	Maverick Chain	https://coinmarketcap.com/currencies/maverick-chain/	0.00543937844471
1026	Aston	https://coinmarketcap.com/currencies/aston/	0.000705104613204
1027	Utrum	https://coinmarketcap.com/currencies/utrum/	0.00896289472988
1028	Rise	https://coinmarketcap.com/currencies/rise/	0.00412989844876
1029	StrongHands	https://coinmarketcap.com/currencies/stronghands/	6.18961480827e-08
1030	Privatix	https://coinmarketcap.com/currencies/privatix/	0.52590731222
1031	Parkgene	https://coinmarketcap.com/currencies/parkgene/	0.00193392109753
1032	savedroid	https://coinmarketcap.com/currencies/savedroid/	0.000211853648141
1033	Blockpass	https://coinmarketcap.com/currencies/blockpass/	0.00338876582231
1034	Happycoin	https://coinmarketcap.com/currencies/happycoin/	0.0262903291495
1035	GlobalBoost-Y	https://coinmarketcap.com/currencies/globalboost-y/	0.0325472213332
1036	Masari	https://coinmarketcap.com/currencies/masari/	0.0486710931502
1037	BZEdge	https://coinmarketcap.com/currencies/bzedge/	0.000188440750908
1038	SnapCoin	https://coinmarketcap.com/currencies/snapcoin/	0.0012848905698
1039	Winco	https://coinmarketcap.com/currencies/winco/	0.00115753037742
1040	Mallcoin	https://coinmarketcap.com/currencies/mallcoin/	0.00315646173162
1041	NOW Token	https://coinmarketcap.com/currencies/now-token/	0.00820018371519
1042	Swarm City	https://coinmarketcap.com/currencies/swarm-city/	0.0648201840397
1043	KARMA	https://coinmarketcap.com/currencies/karma-eos/	0.000103279690356
1044	Fiii	https://coinmarketcap.com/currencies/fiii/	0.00114233659812
1045	FlypMe	https://coinmarketcap.com/currencies/flypme/	0.0312260614419
1046	uPlexa	https://coinmarketcap.com/currencies/uplexa/	0.000311457439434
1047	MinexCoin	https://coinmarketcap.com/currencies/minexcoin/	0.0940248129255
1048	Sharder	https://coinmarketcap.com/currencies/sharder/	0.00193216898038
1049	StarCoin	https://coinmarketcap.com/currencies/starcointv/	0.000360950349095
1050	BitcoinZ	https://coinmarketcap.com/currencies/bitcoinz/	0.000104285034493
1051	wys Token	https://coinmarketcap.com/currencies/wys-token/	0.00528550947715
1052	PHI Token	https://coinmarketcap.com/currencies/phi-token/	0.0926536563001
1053	Karma	https://coinmarketcap.com/currencies/karma/	0.00030156955435
1054	Actinium	https://coinmarketcap.com/currencies/actinium/	0.038957963041
1055	NoLimitCoin	https://coinmarketcap.com/currencies/nolimitcoin/	0.00130947999595
1056	Wibson	https://coinmarketcap.com/currencies/wibson/	0.000198661181974
1057	Denarius	https://coinmarketcap.com/currencies/denarius-dnr/	0.0840129987256
1058	Leverj	https://coinmarketcap.com/currencies/leverj/	0.00443408932299
1059	win.win	https://coinmarketcap.com/currencies/win-win/	0.000201458460915
1060	SnowGem	https://coinmarketcap.com/currencies/snowgem/	0.0294345195676
1061	GeoCoin	https://coinmarketcap.com/currencies/geocoin/	0.163886457955
1062	Membrana	https://coinmarketcap.com/currencies/membrana/	0.0107526037598
1063	QuadrantProtocol	https://coinmarketcap.com/currencies/quadrantprotocol/	0.00155740849177
1064	Karbo	https://coinmarketcap.com/currencies/karbo/	0.0663770990303
1065	LNX Protocol	https://coinmarketcap.com/currencies/lnx-protocol/	0.00190590024607
1066	Shard	https://coinmarketcap.com/currencies/shard/	0.0262903291495
1067	MTC Mesh Network	https://coinmarketcap.com/currencies/mtc-mesh-network/	0.00155817980506
1068	COPYTRACK	https://coinmarketcap.com/currencies/copytrack/	0.0106494890427
1069	Playkey	https://coinmarketcap.com/currencies/playkey/	0.0367672583204
1070	HOQU	https://coinmarketcap.com/currencies/hoqu/	0.00301644284982
1071	Solaris	https://coinmarketcap.com/currencies/solaris/	0.29476994235
1072	OracleChain	https://coinmarketcap.com/currencies/oraclechain/	0.0168896798762
1073	eBoost	https://coinmarketcap.com/currencies/eboostcoin/	0.00505510759526
1074	TraDove B2BCoin	https://coinmarketcap.com/currencies/b2bcoin/	0.00100789027576
1075	ALBOS	https://coinmarketcap.com/currencies/albos/	4.19557203925e-05
1076	ZMINE	https://coinmarketcap.com/currencies/zmine/	0.00303467684102
1077	Shivom	https://coinmarketcap.com/currencies/shivom/	0.00054548454194
1078	GoNetwork	https://coinmarketcap.com/currencies/gonetwork/	0.00681286659218
1079	DOS Network	https://coinmarketcap.com/currencies/dos-network/	0.00512126221121
1080	XPA	https://coinmarketcap.com/currencies/xpa/	0.00851144213587
1081	PAL Network	https://coinmarketcap.com/currencies/pal-network/	0.00110480810508
1082	HEROcoin	https://coinmarketcap.com/currencies/herocoin/	0.00324690062824
1083	Scala	https://coinmarketcap.com/currencies/scala/	5.54252244035e-05
1084	Sakura Bloom	https://coinmarketcap.com/currencies/sakura-bloom/	0.000183156685746
1085	Birake	https://coinmarketcap.com/currencies/birake/	0.00680020843621
1086	ATMChain	https://coinmarketcap.com/currencies/attention-token-of-media/	0.000100806231445
1087	Swap	https://coinmarketcap.com/currencies/swap/	0.0755057000215
1088	Zippie	https://coinmarketcap.com/currencies/zippie/	0.00172628306612
1089	KuboCoin	https://coinmarketcap.com/currencies/kubocoin/	8.01959439153e-06
1090	ACE (TokenStars)	https://coinmarketcap.com/currencies/ace/	0.0392843998785
1091	Ink Protocol	https://coinmarketcap.com/currencies/ink-protocol/	0.00143666054898
1092	AidCoin	https://coinmarketcap.com/currencies/aidcoin/	0.010093997199
1093	DEEX	https://coinmarketcap.com/currencies/deex/	0.00809469093638
1094	ChainX	https://coinmarketcap.com/currencies/chainx/	3.08629933365
1095	Soma	https://coinmarketcap.com/currencies/soma/	0.0467048227707
1096	Linfinity	https://coinmarketcap.com/currencies/linfinity/	0.000501090016202
1097	EUNO	https://coinmarketcap.com/currencies/euno/	0.0168982042609
1098	Gems	https://coinmarketcap.com/currencies/gems-protocol/	0.000389980685244
1099	PlatonCoin	https://coinmarketcap.com/currencies/platoncoin/	0.0809539427484
1100	Carboneum [C8...	https://coinmarketcap.com/currencies/carboneum-c8-token/	0.00868392956225
1101	Amon	https://coinmarketcap.com/currencies/amon/	0.000803875376892
1102	White Standard	https://coinmarketcap.com/currencies/white-standard/	1.0083207116
1103	Sapien	https://coinmarketcap.com/currencies/sapien/	0.00198843028074
1104	Energo	https://coinmarketcap.com/currencies/energo/	0.000727230946561
1105	Plus-Coin	https://coinmarketcap.com/currencies/plus-coin/	0.000805220331338
1106	Freicoin	https://coinmarketcap.com/currencies/freicoin/	0.00787576946071
1107	Miners' Rewar...	https://coinmarketcap.com/currencies/miners-reward-token/	0.0435040395587
1108	Lobstex	https://coinmarketcap.com/currencies/lobstex/	0.0251801564968
1109	Nerva	https://coinmarketcap.com/currencies/nerva/	0.0254844953058
1110	ZEON	https://coinmarketcap.com/currencies/zeon/	1.71684604605e-05
1111	Auroracoin	https://coinmarketcap.com/currencies/auroracoin/	0.0238169627496
1112	EOS TRUST	https://coinmarketcap.com/currencies/eos-trust/	5.71942585632e-05
1113	REAL	https://coinmarketcap.com/currencies/real/	0.0427475262215
1114	OBITS	https://coinmarketcap.com/currencies/obits/	0.0280709153192
1115	Mao Zedong	https://coinmarketcap.com/currencies/mao-zedong/	0.0674885844066
1116	1World	https://coinmarketcap.com/currencies/1world/	0.0204301159852
1117	Jarvis+	https://coinmarketcap.com/currencies/jarvis/	0.00676350797793
1118	HyperSpace	https://coinmarketcap.com/currencies/synereo/	0.00423216946305
1119	AiLink Token	https://coinmarketcap.com/currencies/ailink-token/	8.70847165683e-05
1120	Ivy	https://coinmarketcap.com/currencies/ivy/	0.00133015462284
1121	Cobinhood	https://coinmarketcap.com/currencies/cobinhood/	0.00100729230458
1122	SmileyCoin	https://coinmarketcap.com/currencies/smileycoin/	1.5943597563e-05
1123	BitScreener T...	https://coinmarketcap.com/currencies/bitscreener-token/	0.00259113666154
1124	eBitcoin	https://coinmarketcap.com/currencies/ebtcnew/	0.0218200174295
1125	Equal	https://coinmarketcap.com/currencies/equal/	0.00126462846602
1126	Lunes	https://coinmarketcap.com/currencies/lunes/	0.00272409378273
1127	Zap	https://coinmarketcap.com/currencies/zap/	0.0031135792271
1128	ExclusiveCoin	https://coinmarketcap.com/currencies/exclusivecoin/	0.0719206705468
1129	Maincoin	https://coinmarketcap.com/currencies/maincoin/	0.00192121651115
1130	Pylon Network	https://coinmarketcap.com/currencies/pylon-network/	0.885107748032
1131	Olympus Labs	https://coinmarketcap.com/currencies/olympus-labs/	0.0105321265474
1132	Coinlancer	https://coinmarketcap.com/currencies/coinlancer/	0.00506365841511
1133	Motocoin	https://coinmarketcap.com/currencies/motocoin/	0.0204433589213
1134	Bitcoin Incog...	https://coinmarketcap.com/currencies/bitcoin-incognito/	0.0367068023427
1135	Elite	https://coinmarketcap.com/currencies/1337coin/	1.49999468706e-05
1136	MIB Coin	https://coinmarketcap.com/currencies/mib-coin/	0.00705204495054
1137	EquiTrader	https://coinmarketcap.com/currencies/equitrader/	0.0311476332031
1138	Teloscoin	https://coinmarketcap.com/currencies/teloscoin/	0.00348670778554
1139	ParallelCoin	https://coinmarketcap.com/currencies/parallelcoin/	1.23580608481
1140	Emerald Crypto	https://coinmarketcap.com/currencies/emerald/	0.0202432026495
1141	Uniform Fisca...	https://coinmarketcap.com/currencies/uniform-fiscal-object/	0.000100712450993
1142	Truegame	https://coinmarketcap.com/currencies/tgame/	0.00464169924591
1143	DCORP Utility	https://coinmarketcap.com/currencies/drp-utility/	0.108527694262
1144	Bela	https://coinmarketcap.com/currencies/belacoin/	0.00906412058934
1145	Sprouts	https://coinmarketcap.com/currencies/sprouts/	2.43150032049e-08
1146	MetaMorph	https://coinmarketcap.com/currencies/metamorph/	0.00272220944731
1147	Ethersocial	https://coinmarketcap.com/currencies/ethersocial/	0.0108787568894
1148	B3Coin	https://coinmarketcap.com/currencies/b3coin/	0.000503646152288
1149	Kolion	https://coinmarketcap.com/currencies/kolion/	0.625310509738
1150	Coin Lion	https://coinmarketcap.com/currencies/coin-lion/	0.0116210549689
1151	DubaiCoin	https://coinmarketcap.com/currencies/dubaicoin-dbix/	0.0874329720373
1152	ToaCoin	https://coinmarketcap.com/currencies/toacoin/	0.000100729230458
1153	StakeCubeCoin	https://coinmarketcap.com/currencies/stakecubecoin/	0.215560553179
1154	Noir	https://coinmarketcap.com/currencies/noir/	0.0184351504593
1155	Transcodium	https://coinmarketcap.com/currencies/transcodium/	0.00689823506712
1156	OWNDATA	https://coinmarketcap.com/currencies/owndata/	3.34569843661e-05
1157	MktCoin	https://coinmarketcap.com/currencies/mktcoin/	0.000302577530493
1158	BitCash	https://coinmarketcap.com/currencies/bitcash/	0.0305497846836
1159	Stipend	https://coinmarketcap.com/currencies/stipend/	0.0324348122074
1160	Eristica	https://coinmarketcap.com/currencies/eristica/	0.00211603635271
1161	Seal Network	https://coinmarketcap.com/currencies/seal-network/	0.000707851825082
1162	Nerves	https://coinmarketcap.com/currencies/nerves/	0.000111266796651
1163	TV-TWO	https://coinmarketcap.com/currencies/tv-two/	0.000813289460388
1164	Ethereum Gold...	https://coinmarketcap.com/currencies/ethereum-gold-project/	7.24093593934e-05
1165	Starbase	https://coinmarketcap.com/currencies/starbase/	0.00190725828137
1166	Graviocoin	https://coinmarketcap.com/currencies/graviocoin/	0.000371986227536
1167	Pura	https://coinmarketcap.com/currencies/pura/	0.00201458460915
1168	OptiToken	https://coinmarketcap.com/currencies/optitoken/	0.0125911538072
1169	Experty	https://coinmarketcap.com/currencies/experty/	0.0127913722845
1170	PUBLYTO Token	https://coinmarketcap.com/currencies/publyto-token/	0.000231074486782
1171	Sumokoin	https://coinmarketcap.com/currencies/sumokoin/	0.0342047343233
1172	Swace	https://coinmarketcap.com/currencies/swace/	0.00152864995213
1173	BUZZCoin	https://coinmarketcap.com/currencies/buzzcoin/	1.71429893338e-05
1174	Bethereum	https://coinmarketcap.com/currencies/bethereum/	0.000696137239027
1175	Parachute	https://coinmarketcap.com/currencies/parachute/	0.000981783539612
1176	Qredit	https://coinmarketcap.com/currencies/qredit/	0.000618527940705
1177	Playgroundz	https://coinmarketcap.com/currencies/playgroundz/	0.0118363392226
1178	Faceter	https://coinmarketcap.com/currencies/faceter/	0.000708543450773
1179	SHIELD	https://coinmarketcap.com/currencies/shield-xsh/	0.000649592924858
1180	BlitzPredict	https://coinmarketcap.com/currencies/blitzpredict/	0.000896490151073
1181	CryCash	https://coinmarketcap.com/currencies/crycash/	0.0701868060062
1182	Manna	https://coinmarketcap.com/currencies/manna/	0.000589746080685
1183	PIXEL	https://coinmarketcap.com/currencies/pixel/	0.00551788924367
1184	0xcert	https://coinmarketcap.com/currencies/0xcert/	0.000978675731761
1185	AVINOC	https://coinmarketcap.com/currencies/avinoc/	0.000832865355495
1186	Sphere	https://coinmarketcap.com/currencies/sphere/	0.0257866829972
1187	ZENZO	https://coinmarketcap.com/currencies/zenzo/	0.0333359583147
1188	EncryptoTel [...	https://coinmarketcap.com/currencies/encryptotel/	0.00512856339499
1189	Eroscoin	https://coinmarketcap.com/currencies/eroscoin/	0.00170313693925
1190	Autonio	https://coinmarketcap.com/currencies/autonio/	0.00298846543308
1191	Blockport	https://coinmarketcap.com/currencies/blockport/	0.0059004487299
1192	The ChampCoin	https://coinmarketcap.com/currencies/the-champcoin/	0.00179031452074
1193	On.Live	https://coinmarketcap.com/currencies/on-live/	0.0144895152139
1194	Relex	https://coinmarketcap.com/currencies/relex/	0.000168627870441
1195	Dovu	https://coinmarketcap.com/currencies/dovu/	0.00077781547814
1196	ODUWA	https://coinmarketcap.com/currencies/oduwa/	0.131758136069
1197	LoMoCoin	https://coinmarketcap.com/currencies/lomocoin/	0.00111192699169
1198	Ubcoin Market	https://coinmarketcap.com/currencies/ubcoin-market/	0.000895857107688
1199	TENA	https://coinmarketcap.com/currencies/tena/	0.114831322722
1200	Ergo	https://coinmarketcap.com/currencies/ergo/	0.760817338264
1201	FedoraCoin	https://coinmarketcap.com/currencies/fedoracoin/	1.42378755542e-06
1202	LALA World	https://coinmarketcap.com/currencies/lala-world/	0.00120875076549
1203	adbank	https://coinmarketcap.com/currencies/adbank/	0.000437532747355
1204	CoTrader	https://coinmarketcap.com/currencies/cotrader/	1.90598033277e-05
1205	Honest	https://coinmarketcap.com/currencies/honest/	0.00885228194754
1206	Rivetz	https://coinmarketcap.com/currencies/rivetz/	0.0113723301187
1207	GlobalToken	https://coinmarketcap.com/currencies/globaltoken/	0.00358642120242
1208	Alchemint Sta...	https://coinmarketcap.com/currencies/alchemint-standards/	0.000935620981072
1209	Bigbom	https://coinmarketcap.com/currencies/bigbom/	0.000872811652517
1210	FirstCoin	https://coinmarketcap.com/currencies/firstcoin/	0.00929999
1211	IDEX Membership	https://coinmarketcap.com/currencies/idex-membership/	145.091979316
1212	Bulwark	https://coinmarketcap.com/currencies/bulwark/	0.0194407414783
1213	Mainstream Fo...	https://coinmarketcap.com/currencies/mainstream-for-the-underground/	0.000267791916595
1214	Target Coin	https://coinmarketcap.com/currencies/target-coin/	0.000302187691373
1215	Zero	https://coinmarketcap.com/currencies/zero/	0.041601172179
1216	Crowd Machine	https://coinmarketcap.com/currencies/crowd-machine/	0.000603060972343
1217	BitDegree	https://coinmarketcap.com/currencies/bitdegree/	0.000777245082593
1218	Vetri	https://coinmarketcap.com/currencies/vetri/	0.00112716562352
1219	Sharpay	https://coinmarketcap.com/currencies/sharpay/	0.000274062531509
1220	Olive	https://coinmarketcap.com/currencies/olive/	0.00101898830961
1221	FidentiaX	https://coinmarketcap.com/currencies/fidentiax/	0.00268723651025
1222	Mercury	https://coinmarketcap.com/currencies/mercury/	0.00282041941812
1223	SounDAC	https://coinmarketcap.com/currencies/bitshares-music/	0.018856748076
1224	Magi	https://coinmarketcap.com/currencies/magi/	0.030238901106
1225	VULCANO	https://coinmarketcap.com/currencies/vulcano/	0.0011280817215
1226	Zetacoin	https://coinmarketcap.com/currencies/zetacoin/	0.00159858420923
1227	Hush	https://coinmarketcap.com/currencies/hush/	0.0478917809113
1228	Universe	https://coinmarketcap.com/currencies/universe/	0.00342479383556
1229	PlayGame	https://coinmarketcap.com/currencies/playgame/	0.000307080195273
1230	Zeitcoin	https://coinmarketcap.com/currencies/zeitcoin/	7.28177136222e-06
1231	NEOX	https://coinmarketcap.com/currencies/neox/	0.250127136667
1232	SyncFab	https://coinmarketcap.com/currencies/syncfab/	0.00145390741146
1233	Maxcoin	https://coinmarketcap.com/currencies/maxcoin/	0.00433063539269
1234	JET8	https://coinmarketcap.com/currencies/jet8/	0.000323681980988
1235	Ixcoin	https://coinmarketcap.com/currencies/ixcoin/	0.0125548006909
1236	Dether	https://coinmarketcap.com/currencies/dether/	0.00309621199093
1237	Ryo Currency	https://coinmarketcap.com/currencies/ryo-currency/	0.0187159365841
1238	BitSend	https://coinmarketcap.com/currencies/bitsend/	0.0106642005712
1239	Jesus Coin	https://coinmarketcap.com/currencies/jesus-coin/	1.44851500572e-05
1240	Titan Coin	https://coinmarketcap.com/currencies/titan-coin/	0.000302187691373
1241	Sparkpoint	https://coinmarketcap.com/currencies/sparkpoint/	0.000102098215064
1242	BioCoin	https://coinmarketcap.com/currencies/biocoin/	0.000301909300324
1243	Sether	https://coinmarketcap.com/currencies/sether/	0.0126353504787
1244	Startcoin	https://coinmarketcap.com/currencies/startcoin/	0.00564083690563
1245	Bob's Repair	https://coinmarketcap.com/currencies/bobs-repair/	0.00138420580665
1246	BitClave	https://coinmarketcap.com/currencies/bitclave/	0.000503646152288
1247	Ether-1	https://coinmarketcap.com/currencies/ether-1/	0.00719828621009
1248	Ties.DB	https://coinmarketcap.com/currencies/tiesdb/	0.00604375382746
1249	IXT	https://coinmarketcap.com/currencies/ixledger/	0.0068708724909
1250	TEAM (TokenSt...	https://coinmarketcap.com/currencies/tokenstars/	0.020547115469
1251	TrezarCoin	https://coinmarketcap.com/currencies/trezarcoin/	0.0014113461517
1252	Elcoin	https://coinmarketcap.com/currencies/elcoin-el/	0.0215560553179
1253	Iconiq Lab Token	https://coinmarketcap.com/currencies/iconiq-lab-token/	0.0622869763515
1254	VeriumReserve	https://coinmarketcap.com/currencies/veriumreserve/	0.102240168915
1255	HeartBout	https://coinmarketcap.com/currencies/heartbout/	0.00449139450291
1256	Trollcoin	https://coinmarketcap.com/currencies/trollcoin/	0.000402916921831
1257	Deutsche eMark	https://coinmarketcap.com/currencies/deutsche-emark/	0.00443134784368
1258	HelloGold	https://coinmarketcap.com/currencies/hellogold/	0.000900625985363
1259	KekCoin	https://coinmarketcap.com/currencies/kekcoin/	0.0220597014702
1260	Scorum Coins	https://coinmarketcap.com/currencies/scorum-coins/	0.00805923447329
1261	FoldingCoin	https://coinmarketcap.com/currencies/foldingcoin/	0.000302187691373
1262	Incodium	https://coinmarketcap.com/currencies/incodium/	2.51576995722e-05
1263	Internet of P...	https://coinmarketcap.com/currencies/internet-of-people/	0.0173634753629
1264	HBZ coin	https://coinmarketcap.com/currencies/hbz-coin/	0.000238047170889
1265	Pesetacoin	https://coinmarketcap.com/currencies/pesetacoin/	0.00166642956691
1266	BlueCoin	https://coinmarketcap.com/currencies/bluecoin/	0.000402849803971
1267	Verify	https://coinmarketcap.com/currencies/verify/	0.0171239691778
1268	LatiumX	https://coinmarketcap.com/currencies/latiumx/	0.0022041505597
1269	Birdchain	https://coinmarketcap.com/currencies/birdchain/	0.00154334476503
1270	Lampix	https://coinmarketcap.com/currencies/lampix/	0.00169212725474
1271	LanaCoin	https://coinmarketcap.com/currencies/lanacoin/	0.000207483741007
1272	FujiCoin	https://coinmarketcap.com/currencies/fujicoin/	0.000100729230458
1273	AdHive	https://coinmarketcap.com/currencies/adhive/	0.00172591521956
1274	Indorse Token	https://coinmarketcap.com/currencies/indorse-token/	0.00604265755937
1275	ClearPoll	https://coinmarketcap.com/currencies/clearpoll/	0.032181170077
1276	CoinMetro Token	https://coinmarketcap.com/currencies/coinmetro-token/	0.0264138579031
1277	Decimated	https://coinmarketcap.com/currencies/decimated/	0.00407000655559
1278	XGOX	https://coinmarketcap.com/currencies/xgox/	9.41186075565e-05
1279	Mithril Ore	https://coinmarketcap.com/currencies/mithril-ore/	17.5426714568
1280	DopeCoin	https://coinmarketcap.com/currencies/dopecoin/	0.00191353656886
1281	Master Contra...	https://coinmarketcap.com/currencies/master-contract-token/	0.000390149557754
1282	Ethouse	https://coinmarketcap.com/currencies/ethouse/	0.00197557577845
1283	HashNet BitEco	https://coinmarketcap.com/currencies/hashnet-biteco/	0.00737263502427
1284	Connect Coin	https://coinmarketcap.com/currencies/connect-coin/	0.00559550984133
1285	SoMee.Social	https://coinmarketcap.com/currencies/ongsocial/	0.00355213514865
1286	DAV Coin	https://coinmarketcap.com/currencies/dav-coin/	0.000339884935825
1287	TrumpCoin	https://coinmarketcap.com/currencies/trumpcoin/	0.0326362706683
1288	Lethean	https://coinmarketcap.com/currencies/lethean/	0.000302187691373
1289	WorldCoin	https://coinmarketcap.com/currencies/worldcoin/	0.00178748709817
1290	Tokenbox	https://coinmarketcap.com/currencies/tokenbox/	0.0187633170411
1291	Expanse	https://coinmarketcap.com/currencies/expanse/	0.0200526039874
1292	HeroNode	https://coinmarketcap.com/currencies/heronode/	0.000195758951078
1293	Bayan Token	https://coinmarketcap.com/currencies/bayan-token/	0.881682954196
1294	Zennies	https://coinmarketcap.com/currencies/zennies/	0.000208003805153
1295	CYCLEAN	https://coinmarketcap.com/currencies/cyclean/	0.000306403763789
1296	Aditus	https://coinmarketcap.com/currencies/aditus/	0.000878804182641
1297	PutinCoin	https://coinmarketcap.com/currencies/putincoin/	0.000250692391719
1298	MFCoin	https://coinmarketcap.com/currencies/mfcoin/	0.00977073535439
1299	GoPower	https://coinmarketcap.com/currencies/gopower/	0.00251411492577
1300	Snovian.Space	https://coinmarketcap.com/currencies/snov/	0.000687743905893
1301	SiaCashCoin	https://coinmarketcap.com/currencies/siacashcoin/	2.5222866952e-05
1302	Jetcoin	https://coinmarketcap.com/currencies/jetcoin/	0.0274990799149
1303	ZCore	https://coinmarketcap.com/currencies/zcore/	0.0422602362988
1304	Litecoin Plus	https://coinmarketcap.com/currencies/litecoin-plus/	0.080052957689
1305	Arbidex	https://coinmarketcap.com/currencies/arbidex/	0.00979312887618
1306	UChain	https://coinmarketcap.com/currencies/uchain/	0.000650419525668
1307	Phoenixcoin	https://coinmarketcap.com/currencies/phoenixcoin/	0.00271381316838
1308	Energycoin	https://coinmarketcap.com/currencies/energycoin/	0.00161139921588
1309	RealChain	https://coinmarketcap.com/currencies/realchain/	0.000479651351907
1310	SixEleven	https://coinmarketcap.com/currencies/sixeleven/	0.409922839385
1311	Invacio	https://coinmarketcap.com/currencies/invacio/	0.00665537286052
1312	SnodeCoin	https://coinmarketcap.com/currencies/snodecoin/	0.00564083690563
1313	Yocoin	https://coinmarketcap.com/currencies/yocoin/	0.000526900941321
1314	View	https://coinmarketcap.com/currencies/view/	0.00554010767517
1315	Bitether	https://coinmarketcap.com/currencies/bitether/	0.00342479383556
1316	Commercium	https://coinmarketcap.com/currencies/commercium/	0.00432744325839
1317	Silent Notary	https://coinmarketcap.com/currencies/silent-notary/	2.29619814189e-06
1318	Dinastycoin	https://coinmarketcap.com/currencies/dinastycoin/	0.000100729230458
1319	The Currency ...	https://coinmarketcap.com/currencies/the-currency-analytics/	0.00155505247939
1320	Auxilium	https://coinmarketcap.com/currencies/auxilium/	0.00167382405511
1321	Gravity	https://coinmarketcap.com/currencies/gravity/	0.000100729230458
1322	Capricoin	https://coinmarketcap.com/currencies/capricoin/	0.0936766083635
1323	Version	https://coinmarketcap.com/currencies/version/	0.000317138208625
1324	SF Capital	https://coinmarketcap.com/currencies/sf-capital/	0.00423062767922
1325	PikcioChain	https://coinmarketcap.com/currencies/pikciochain/	0.00368426202334
1326	Bitcoin CZ	https://coinmarketcap.com/currencies/bitcoin-cz/	0.0763607243769
1327	CannabisCoin	https://coinmarketcap.com/currencies/cannabiscoin/	0.00237350803756
1328	Gentarium	https://coinmarketcap.com/currencies/gentarium/	0.0500946757363
1329	Crypto Sports	https://coinmarketcap.com/currencies/crypto-sports/	0.102905993447
1330	Netko	https://coinmarketcap.com/currencies/netko/	0.0211531383961
1331	REBL	https://coinmarketcap.com/currencies/rebl/	0.00103801763747
1332	InsaneCoin	https://coinmarketcap.com/currencies/insanecoin-insn/	0.00755469228433
1333	BlockCAT	https://coinmarketcap.com/currencies/blockcat/	0.0241843386168
1334	CryptoCarbon	https://coinmarketcap.com/currencies/cryptocarbon/	0.00717551531814
1335	Arionum	https://coinmarketcap.com/currencies/arionum/	0.00110802153503
1336	Crave	https://coinmarketcap.com/currencies/crave/	0.00805829485031
1337	Formosa Finan...	https://coinmarketcap.com/currencies/formosa-financial/	0.000204387213082
1338	ANON	https://coinmarketcap.com/currencies/anon/	0.0231664277519
1339	Devery	https://coinmarketcap.com/currencies/devery/	0.00279493322866
1340	CREDIT	https://coinmarketcap.com/currencies/credit/	1.90849208493e-05
1341	eSDChain	https://coinmarketcap.com/currencies/esdchain/	0.00164971406954
1342	Bitibu Coin	https://coinmarketcap.com/currencies/bitibu-coin/	0.0407681690493
1343	Kuende	https://coinmarketcap.com/currencies/kuende/	0.000262790596571
1344	BoatPilot Token	https://coinmarketcap.com/currencies/boat-pilot-token/	0.00232780708103
1345	Bitzeny	https://coinmarketcap.com/currencies/bitzeny/	0.00227149661517
1346	Cubiex	https://coinmarketcap.com/currencies/cubiex/	0.00856914775723
1347	Helleniccoin	https://coinmarketcap.com/currencies/helleniccoin/	0.00241750153098
1348	Emphy	https://coinmarketcap.com/currencies/emphy/	0.021177559253
1349	Goodomy	https://coinmarketcap.com/currencies/goodomy/	0.000269773721065
1350	WIZBL	https://coinmarketcap.com/currencies/wizbl/	0.00110802153503
1351	Travelflex	https://coinmarketcap.com/currencies/travelflex/	0.0021
1352	Ignition	https://coinmarketcap.com/currencies/ignition/	0.162059174558
1353	Moneynet	https://coinmarketcap.com/currencies/moneynet/	4.1970970825e-05
1354	FantasyGold	https://coinmarketcap.com/currencies/fantasygold/	0.0101336165903
1355	DraftCoin	https://coinmarketcap.com/currencies/draftcoin/	0.0188784
1356	Niobio Cash	https://coinmarketcap.com/currencies/niobio-cash/	0.00121846868131
1357	Memetic / Pep...	https://coinmarketcap.com/currencies/memetic/	0.00545488213996
1358	Bitstar	https://coinmarketcap.com/currencies/bitstar/	0.00791597202253
1359	Rupee	https://coinmarketcap.com/currencies/rupee/	0.0045328153706
1360	EDRCoin	https://coinmarketcap.com/currencies/edrcoin/	0.0545384109339
1361	ShareX	https://coinmarketcap.com/currencies/sharex/	0.000247368129089
1362	FSBT API Token	https://coinmarketcap.com/currencies/fsbt-api-token/	0.0452701472502
1363	Shadow Token	https://coinmarketcap.com/currencies/shadow-token/	0.0226242536245
1364	Unify	https://coinmarketcap.com/currencies/unify/	0.00866271381936
1365	Hercules	https://coinmarketcap.com/currencies/hercules/	0.00350282740171
1366	LiteDoge	https://coinmarketcap.com/currencies/litedoge/	1.02627408094e-05
1367	EtherGem	https://coinmarketcap.com/currencies/ethergem/	0.00799369610261
1368	Matchpool	https://coinmarketcap.com/currencies/guppy/	0.00206914475106
1369	Nitro	https://coinmarketcap.com/currencies/nitro/	0.00163065155085
1370	BetterBetting	https://coinmarketcap.com/currencies/betterbetting/	0.00082537531437
1371	CryptoAds Mar...	https://coinmarketcap.com/currencies/cryptoads-marketplace/	0.105163003773
1372	Galilel	https://coinmarketcap.com/currencies/galilel/	0.00840999263188
1373	Obsidian	https://coinmarketcap.com/currencies/obsidian/	0.00221604307007
1374	Banyan Network	https://coinmarketcap.com/currencies/banyan-network/	0.000247810145702
1375	Atonomi	https://coinmarketcap.com/currencies/atonomi/	0.000304007701903
1376	PoSW Coin	https://coinmarketcap.com/currencies/posw-coin/	0.00336188542546
1377	TrakInvest	https://coinmarketcap.com/currencies/trakinvest/	0.0017615407679
1378	GoByte	https://coinmarketcap.com/currencies/gobyte/	0.0401487077599
1379	Universal Cur...	https://coinmarketcap.com/currencies/universal-currency/	0.00906563074119
1380	WPP TOKEN	https://coinmarketcap.com/currencies/wpp-token/	0.000508561354736
1381	EverGreenCoin	https://coinmarketcap.com/currencies/evergreencoin/	0.0101736522762
1382	Blocktix	https://coinmarketcap.com/currencies/blocktix/	0.00355925365596
1383	FORCE	https://coinmarketcap.com/currencies/force/	0.00100729230458
1384	iDealCash	https://coinmarketcap.com/currencies/idealcash/	0.000100729230458
1385	Narrative	https://coinmarketcap.com/currencies/narrative/	0.0033626097984
1386	TRONCLASSIC	https://coinmarketcap.com/currencies/tronclassic/	2.98474904351e-07
1387	HyperStake	https://coinmarketcap.com/currencies/hyperstake/	0.000100729230458
1388	Synergy	https://coinmarketcap.com/currencies/synergy/	0.028012531805
1389	ProxyNode	https://coinmarketcap.com/currencies/proxynode/	0.00109613740083
1390	Bitcoiin	https://coinmarketcap.com/currencies/bitcoiin/	0.00259206099702
1391	Condensate	https://coinmarketcap.com/currencies/condensate/	0.00010878986296
1392	bitcoin2network	https://coinmarketcap.com/currencies/bitcoin2network/	0.000102760568482
1393	DigitalPrice	https://coinmarketcap.com/currencies/digitalprice/	0.00684958767112
1394	SIMDAQ	https://coinmarketcap.com/currencies/simdaq/	0.00768655019117
1395	VoteCoin	https://coinmarketcap.com/currencies/votecoin/	0.00213038091175
1396	PopularCoin	https://coinmarketcap.com/currencies/popularcoin/	3.35453887805e-05
1397	Tokes	https://coinmarketcap.com/currencies/tokes/	0.100427330182
1398	Credit Tag Chain	https://coinmarketcap.com/currencies/credit-tag-chain/	0.00224877296875
1399	Speed Mining ...	https://coinmarketcap.com/currencies/speed-mining-service/	1.26092587668
1400	TransferCoin	https://coinmarketcap.com/currencies/transfercoin/	0.0163181353341
1401	Bitblocks	https://coinmarketcap.com/currencies/bitblocks/	0.00110377442394
1402	Neutron	https://coinmarketcap.com/currencies/neutron/	0.00331590659408
1403	AquariusCoin	https://coinmarketcap.com/currencies/aquariuscoin/	0.0516388029793
1404	TittieCoin	https://coinmarketcap.com/currencies/tittiecoin/	0.000100729230458
1405	Save Environm...	https://coinmarketcap.com/currencies/save-environment-token/	0.131819901344
1406	SRCOIN	https://coinmarketcap.com/currencies/srcoin/	2.49563434803e-05
1407	PENG	https://coinmarketcap.com/currencies/peng/	1.76508286738e-05
1408	PKG Token	https://coinmarketcap.com/currencies/pkg-token/	1.39894322029e-05
1409	Darcrus	https://coinmarketcap.com/currencies/darcrus/	0.00922383973193
1410	Spectiv	https://coinmarketcap.com/currencies/signal-token/	0.000519279419677
1411	PeepCoin	https://coinmarketcap.com/currencies/peepcoin/	1.92631475861e-06
1412	imbrex	https://coinmarketcap.com/currencies/imbrex/	0.0143464360138
1413	WABnetwork	https://coinmarketcap.com/currencies/wabnetwork/	1.41020922641e-05
1414	bitEUR	https://coinmarketcap.com/currencies/biteur/	1.13936755916
1929	iBank	https://coinmarketcap.com/currencies/ibank/	0.00090642203695
1415	RefToken	https://coinmarketcap.com/currencies/reftoken/	0.121931132119
1416	Aphelion	https://coinmarketcap.com/currencies/aphelion/	0.00241807979802
1417	InvestFeed	https://coinmarketcap.com/currencies/investfeed/	0.000630424143341
1418	Stakinglab	https://coinmarketcap.com/currencies/stakinglab/	0.296113235135
1419	Soarcoin	https://coinmarketcap.com/currencies/soarcoin/	0.00010119584039
1420	Wispr	https://coinmarketcap.com/currencies/wispr/	0.00390681139172
1421	Centauri	https://coinmarketcap.com/currencies/centauri/	0.00282041845281
1422	EventChain	https://coinmarketcap.com/currencies/eventchain/	0.00380565591369
1423	GINcoin	https://coinmarketcap.com/currencies/gincoin/	0.0169525499567
1424	bitqy	https://coinmarketcap.com/currencies/bitqy/	3.79531811059e-05
1425	TrueDeck	https://coinmarketcap.com/currencies/truedeck/	0.00381982609045
1426	Carboncoin	https://coinmarketcap.com/currencies/carboncoin/	7.6e-06
1427	JSECOIN	https://coinmarketcap.com/currencies/jsecoin/	0.000262676744598
1428	GCN Coin	https://coinmarketcap.com/currencies/gcn-coin/	6.72413630211e-07
1429	Social Activi...	https://coinmarketcap.com/currencies/social-activity-token/	0.000906563074119
1430	BlockMesh	https://coinmarketcap.com/currencies/blockmesh/	0.000421551829465
1431	XMCT	https://coinmarketcap.com/currencies/xmct/	0.00111386681462
1432	BitNautic Token	https://coinmarketcap.com/currencies/bitnautic-token/	0.0078568799757
1433	WandX	https://coinmarketcap.com/currencies/wandx/	0.00937890264164
1434	Hype Token	https://coinmarketcap.com/currencies/hype-token/	0.00261830124514
1435	ICO OpenLedger	https://coinmarketcap.com/currencies/ico-openledger/	0.245066449536
1436	Ethereum Cash	https://coinmarketcap.com/currencies/ethereumcash/	0.00808284203907
1437	IP Exchange	https://coinmarketcap.com/currencies/ip-exchange/	0.000120602288526
1438	Pedity	https://coinmarketcap.com/currencies/pedity/	8.29060834454e-05
1439	Giant	https://coinmarketcap.com/currencies/giant-coin/	0.0195958506419
1440	Golos Gold	https://coinmarketcap.com/currencies/golos-gold/	0.00886417228028
1441	MyBit	https://coinmarketcap.com/currencies/mybit/	0.000733844173459
1442	MyWish	https://coinmarketcap.com/currencies/mywish/	0.0185522040385
1443	bitBTC	https://coinmarketcap.com/currencies/bitbtc/	2754.098454
1444	EXMR	https://coinmarketcap.com/currencies/exmr/	0.00950838791865
1445	Exosis	https://coinmarketcap.com/currencies/exosis/	0.423415300397
1446	DogeCash	https://coinmarketcap.com/currencies/dogecash/	0.0303013112317
1447	Repme	https://coinmarketcap.com/currencies/repme/	1.77962682798e-06
1448	Opus	https://coinmarketcap.com/currencies/opus/	0.000778636951438
1449	DeviantCoin	https://coinmarketcap.com/currencies/deviantcoin/	0.00703578066985
1450	Social Send	https://coinmarketcap.com/currencies/social-send/	0.00280755951675
1451	Worldcore	https://coinmarketcap.com/currencies/worldcore/	0.000607139293111
1452	Bonpay	https://coinmarketcap.com/currencies/bonpay/	0.00956927689348
1453	ARBITRAGE	https://coinmarketcap.com/currencies/arbitrage/	0.0256257898983
1454	AllSafe	https://coinmarketcap.com/currencies/allsafe/	0.0136198435981
1455	Evedo	https://coinmarketcap.com/currencies/evedo/	0.0153767674533
1456	Bitradio	https://coinmarketcap.com/currencies/bitradio/	0.0135984461118
1457	More Coin	https://coinmarketcap.com/currencies/more-coin/	0.0532857629121
1458	Menlo One	https://coinmarketcap.com/currencies/menlo-one/	0.000353927918176
1459	Level Up Coin	https://coinmarketcap.com/currencies/level-up/	0.00010529351464
1460	Apollon	https://coinmarketcap.com/currencies/apollon/	0.000704516947507
1461	Photon	https://coinmarketcap.com/currencies/photon/	3.46072929101e-06
1462	Pakcoin	https://coinmarketcap.com/currencies/pakcoin/	0.00151318372326
1463	Bee Token	https://coinmarketcap.com/currencies/bee-token/	0.000435060669665
1464	WavesGo	https://coinmarketcap.com/currencies/wavesgo/	0.0134007987744
1465	Naviaddress	https://coinmarketcap.com/currencies/naviaddress/	0.000423240315961
1466	Civitas	https://coinmarketcap.com/currencies/civitas/	0.0146057384164
1467	GravityCoin	https://coinmarketcap.com/currencies/gravitycoin/	0.0402791234454
1468	Bridge Protocol	https://coinmarketcap.com/currencies/bridge-protocol/	0.000452422577717
1469	SwiftCash	https://coinmarketcap.com/currencies/swiftcash/	0.00100729230458
1470	Iungo	https://coinmarketcap.com/currencies/iungo/	0.00251300501418
1471	BitcoiNote	https://coinmarketcap.com/currencies/bitcoinote/	0.00933871772978
1472	Block Array	https://coinmarketcap.com/currencies/block-array/	0.00145228427336
1473	Opal	https://coinmarketcap.com/currencies/opal/	0.00653434803717
1474	AudioCoin	https://coinmarketcap.com/currencies/audiocoin/	0.000100784769939
1475	StrongHands M...	https://coinmarketcap.com/currencies/stronghands-masternode/	0.066771068807
1476	Adelphoi	https://coinmarketcap.com/currencies/adelphoi/	0.00473427383151
1477	IGToken	https://coinmarketcap.com/currencies/igtoken/	3.103669188e-05
1478	Advanced Tech...	https://coinmarketcap.com/currencies/arcticcoin/	0.00372698152693
1479	Block-Logic	https://coinmarketcap.com/currencies/block-logic/	0.0042279018989
1480	Guaranteed Et...	https://coinmarketcap.com/currencies/guaranteed-ethurance-token-extra/	0.000322312426561
1481	Leadcoin	https://coinmarketcap.com/currencies/leadcoin/	0.000122430952993
1482	Bitcoin Scrypt	https://coinmarketcap.com/currencies/bitcoin-scrypt/	0.00542684986763
1483	Anoncoin	https://coinmarketcap.com/currencies/anoncoin/	0.0451253331438
1484	Kalkulus	https://coinmarketcap.com/currencies/kalkulus/	0.00574157836612
1485	Magnet	https://coinmarketcap.com/currencies/magnet/	0.00201458460915
1486	Newton Coin P...	https://coinmarketcap.com/currencies/newton-coin-project/	5.22212509648e-07
1487	TrustNote	https://coinmarketcap.com/currencies/trustnote/	0.000302132937193
1488	Bankcoin	https://coinmarketcap.com/currencies/bankcoin/	0.00909832349168
1489	Bitnation	https://coinmarketcap.com/currencies/bitnation/	3.61316279843e-06
1490	PiplCoin	https://coinmarketcap.com/currencies/piplcoin/	0.00111564442599
1491	IOTW	https://coinmarketcap.com/currencies/iotw/	0.00279591463211
1492	Advanced Inte...	https://coinmarketcap.com/currencies/advanced-internet-blocks/	0.00281950785736
1493	VeriME	https://coinmarketcap.com/currencies/verime/	0.000519437320703
1494	Globatalent	https://coinmarketcap.com/currencies/globatalent/	0.000183301563282
1495	WXCOINS	https://coinmarketcap.com/currencies/wxcoins/	0.0163324166684
1496	MMOCoin	https://coinmarketcap.com/currencies/mmocoin/	0.00152676521964
1497	Suretly	https://coinmarketcap.com/currencies/suretly/	0.385263219441
1498	BitBar	https://coinmarketcap.com/currencies/bitbar/	2.10213287638
1499	Elysian	https://coinmarketcap.com/currencies/elysian/	0.00090730902849
1500	Bitcoin Turbo...	https://coinmarketcap.com/currencies/bitcoin-turbo-koin/	5.36243873726e-06
1501	IOTW	https://coinmarketcap.com/currencies/iotw/	0.00279591463211
1502	Asian Dragon	https://coinmarketcap.com/currencies/asian-dragon/	0.0014628532526
1503	Agrolot	https://coinmarketcap.com/currencies/agrolot/	0.00191362650722
1504	Dash Green	https://coinmarketcap.com/currencies/dash-green/	0.0380388841415
1505	ArbitrageCT	https://coinmarketcap.com/currencies/arbitragect/	0.000834911902464
1506	ModulTrade	https://coinmarketcap.com/currencies/modultrade/	0.00231677230053
1507	Webchain	https://coinmarketcap.com/currencies/webchain/	0.000604375382746
1508	Kobocoin	https://coinmarketcap.com/currencies/kobocoin/	0.00343376459152
1509	Iridium	https://coinmarketcap.com/currencies/iridium/	0.00453213621486
1510	HyperQuant	https://coinmarketcap.com/currencies/hyperquant/	0.000947611826654
1511	Auctus	https://coinmarketcap.com/currencies/auctus/	0.0028167034891
1512	RPICoin	https://coinmarketcap.com/currencies/rpicoin/	0.000100729230458
1513	Bitcloud	https://coinmarketcap.com/currencies/bitcloud/	0.00271968922236
1514	Fabric Token	https://coinmarketcap.com/currencies/fabric-token/	0.00338629728244
1515	BLAST	https://coinmarketcap.com/currencies/blast/	0.00158985225068
1516	No BS Crypto	https://coinmarketcap.com/currencies/no-bs-crypto/	6.64468753978e-05
1517	Freyrchain	https://coinmarketcap.com/currencies/freyrchain/	0.000165122435605
1518	Galactrum	https://coinmarketcap.com/currencies/galactrum/	0.0190378245565
1519	Webcoin	https://coinmarketcap.com/currencies/webcoin/	0.00208134165485
1520	BoutsPro	https://coinmarketcap.com/currencies/boutspro/	0.00107316361763
1521	ChessCoin	https://coinmarketcap.com/currencies/chesscoin/	0.00152105567134
1522	Chronologic	https://coinmarketcap.com/currencies/chronologic/	0.0893760133198
1523	Viuly	https://coinmarketcap.com/currencies/viuly/	0.000105061174455
1524	Vivid Coin	https://coinmarketcap.com/currencies/vivid-coin/	0.0136661354083
1525	Monkey Project	https://coinmarketcap.com/currencies/monkey-project/	0.010778027659
1526	Rimbit	https://coinmarketcap.com/currencies/rimbit/	0.000402916921831
1527	TagCoin	https://coinmarketcap.com/currencies/tagcoin/	0.0123441806772
1528	Profile Utili...	https://coinmarketcap.com/currencies/profile-utility-token/	0.00175551037146
1529	SkyHub Coin	https://coinmarketcap.com/currencies/skyhub-coin/	0.161948635323
1530	Rentberry	https://coinmarketcap.com/currencies/rentberry/	0.000260377780716
1531	Impact	https://coinmarketcap.com/currencies/impact/	0.000706483758415
1532	Daneel	https://coinmarketcap.com/currencies/daneel/	0.0038427680767
1533	Digitalcoin	https://coinmarketcap.com/currencies/digitalcoin/	0.00231638637283
1534	Megacoin	https://coinmarketcap.com/currencies/megacoin/	0.0020241210673
1535	Adzcoin	https://coinmarketcap.com/currencies/adzcoin/	0.00157828517608
1536	Swing	https://coinmarketcap.com/currencies/swing/	0.0175268860996
1537	BBSCoin	https://coinmarketcap.com/currencies/bbscoin/	9.123251661e-07
1538	NetKoin	https://coinmarketcap.com/currencies/netkoin/	1.71214763815e-05
1539	Sociall	https://coinmarketcap.com/currencies/sociall/	0.00454288829364
1540	Alt.Estate token	https://coinmarketcap.com/currencies/alt-estate-token/	0.000103751107371
1541	Beacon	https://coinmarketcap.com/currencies/beacon/	0.00765542151478
1542	Uptrennd	https://coinmarketcap.com/currencies/uptrennd/	0.0161420212225
1543	Jin Coin	https://coinmarketcap.com/currencies/jin-coin/	0.00733118558384
1544	Regalcoin	https://coinmarketcap.com/currencies/regalcoin/	0.00570412510529
1545	Ultimate Secu...	https://coinmarketcap.com/currencies/ultimate-secure-cash/	0.00705104613204
1546	Rubies	https://coinmarketcap.com/currencies/rubies/	0.00700057372299
1547	AirWire	https://coinmarketcap.com/currencies/airwire/	0.000604646891966
1548	Coinchase	https://coinmarketcap.com/currencies/coinchase/	4.1970970825e-05
1549	Doge Token	https://coinmarketcap.com/currencies/doge-token/	8.11306165075e-06
1550	MODEL-X-coin	https://coinmarketcap.com/currencies/model-x-coin/	0.00596101522911
1551	EurocoinToken	https://coinmarketcap.com/currencies/eurocoin-token/	0.0430076283199
1552	Cryptonite	https://coinmarketcap.com/currencies/cryptonite/	0.000100729230458
1553	Mincoin	https://coinmarketcap.com/currencies/mincoin/	0.0121862065701
1554	ZeusNetwork	https://coinmarketcap.com/currencies/zeusnetwork/	1.00729230458e-06
1555	Bitcoin Red	https://coinmarketcap.com/currencies/bitcoin-red/	0.00340045105576
1556	Evil Coin	https://coinmarketcap.com/currencies/evil-coin/	0.00331541107822
1557	EnterCoin	https://coinmarketcap.com/currencies/entercoin/	0.0231863111738
1558	SPIDER VPS	https://coinmarketcap.com/currencies/spider-vps/	0.0240764374155
1559	Elixir	https://coinmarketcap.com/currencies/elixir/	0.00195448921834
1560	CyberFM	https://coinmarketcap.com/currencies/cyberfm/	1.34911765478e-06
1561	BTCtalkcoin	https://coinmarketcap.com/currencies/btctalkcoin/	0.0010547177252
1562	CDX Network	https://coinmarketcap.com/currencies/cdx-network/	0.00211531383961
1563	SHPING	https://coinmarketcap.com/currencies/shping/	8.36424609151e-05
1564	Billionaire T...	https://coinmarketcap.com/currencies/billionaire-token/	0.0206900229139
1565	ATBCoin	https://coinmarketcap.com/currencies/atbcoin/	0.00163020988062
1566	Datarius Credit	https://coinmarketcap.com/currencies/datarius-credit/	0.000535805444375
1567	Minereum	https://coinmarketcap.com/currencies/minereum/	0.00997219381531
1568	BTC Lite	https://coinmarketcap.com/currencies/btc-lite/	0.00362625229648
1569	ProCurrency	https://coinmarketcap.com/currencies/procurrency/	0.000654639268744
1570	BriaCoin	https://coinmarketcap.com/currencies/briacoin/	0.0898267110113
1571	HYPNOXYS	https://coinmarketcap.com/currencies/hypnoxys/	3.34e-06
1572	Thore Cash	https://coinmarketcap.com/currencies/thore-cash/	0.00120118308241
1573	ALLUVA	https://coinmarketcap.com/currencies/alluva/	0.00774189052734
1574	Titcoin	https://coinmarketcap.com/currencies/titcoin/	0.00100753892371
1575	OPCoinX	https://coinmarketcap.com/currencies/opcoinx/	0.000402537640917
1576	Vsync	https://coinmarketcap.com/currencies/vsync-vsx/	0.000404117892508
1577	BLOC.MONEY	https://coinmarketcap.com/currencies/bloc-money/	0.00604375382746
1578	PRiVCY	https://coinmarketcap.com/currencies/privcy/	0.00392227297891
1579	Decision Token	https://coinmarketcap.com/currencies/decision-token/	0.0020154084324
1580	GenesisX	https://coinmarketcap.com/currencies/genesisx/	0.00735385563655
1581	TravelNote	https://coinmarketcap.com/currencies/travelnote/	0.0294727218861
1582	PrimeStone	https://coinmarketcap.com/currencies/primestone/	0.003015432064
1583	Helium	https://coinmarketcap.com/currencies/helium/	0.0114831322722
1584	Bitcoin Zero	https://coinmarketcap.com/currencies/bitcoin-zero/	0.00296071297456
1585	Herbalist Token	https://coinmarketcap.com/currencies/herbalist-token/	6.51245855259e-06
1586	Decentralized...	https://coinmarketcap.com/currencies/decentralized-machine-learning/	0.000983190433655
1587	bitSilver	https://coinmarketcap.com/currencies/bitsilver/	2.82015982413
1588	vSlice	https://coinmarketcap.com/currencies/vslice/	0.00176893939475
1589	Blockburn	https://coinmarketcap.com/currencies/blockburn/	0.0999769527136
1590	InterValue	https://coinmarketcap.com/currencies/intervalue/	0.000457383505226
1591	Gold Poker	https://coinmarketcap.com/currencies/gold-poker/	0.0140368335994
1592	BitWhite	https://coinmarketcap.com/currencies/bitwhite/	0.00159233365547
1593	PRASM	https://coinmarketcap.com/currencies/prasm/	2.55182445056e-05
1594	ArtByte	https://coinmarketcap.com/currencies/artbyte/	7.23159584845e-05
1595	STRAKS	https://coinmarketcap.com/currencies/straks/	0.00239691750129
1596	TOKYO	https://coinmarketcap.com/currencies/tokyo/	0.000209289646362
1597	CROAT	https://coinmarketcap.com/currencies/croat/	0.000805833843661
1598	MicroMoney	https://coinmarketcap.com/currencies/micromoney/	0.00351960086523
1599	PitisCoin	https://coinmarketcap.com/currencies/pitiscoin/	0.000100729230458
1600	Gexan	https://coinmarketcap.com/currencies/gexan/	0.0525135470156
1601	BritCoin	https://coinmarketcap.com/currencies/britcoin/	0.00258327900595
1602	Xuez	https://coinmarketcap.com/currencies/xuez/	0.0174261507648
1603	Aigang	https://coinmarketcap.com/currencies/aigang/	0.00186932334179
1604	iTicoin	https://coinmarketcap.com/currencies/iticoin/	1.70967722856
1605	ClearCoin	https://coinmarketcap.com/currencies/clearcoin/	0.000103146731989
1606	CrowdWiz	https://coinmarketcap.com/currencies/crowdwiz/	0.00711253978296
1607	SkinCoin	https://coinmarketcap.com/currencies/skincoin/	0.000616197110472
1608	2GIVE	https://coinmarketcap.com/currencies/2give/	0.000103437204727
1609	International...	https://coinmarketcap.com/currencies/internationalcryptox/	0.000125309825748
1610	Monoeci	https://coinmarketcap.com/currencies/monacocoin/	0.00651893848278
1611	GoHelpFund	https://coinmarketcap.com/currencies/gohelpfund/	0.00433135690968
1612	EtherSportz	https://coinmarketcap.com/currencies/ethersportz/	0.0172209058722
1613	Ratecoin	https://coinmarketcap.com/currencies/ratecoin/	0.000422001121444
1614	SuperCoin	https://coinmarketcap.com/currencies/supercoin/	0.00100729230458
1615	Cashpayz Token	https://coinmarketcap.com/currencies/cashpayz-token/	0.0285220253551
1616	GuccioneCoin	https://coinmarketcap.com/currencies/guccionecoin/	0.00251570814842
1617	Etheera	https://coinmarketcap.com/currencies/etheera/	7.08291477493e-06
1618	Sugar Exchange	https://coinmarketcap.com/currencies/sugar-exchange/	0.00111226676749
1619	bitGold	https://coinmarketcap.com/currencies/bitgold/	264.263607208
1620	Orbis Token	https://coinmarketcap.com/currencies/orbis-token/	0.00258999971417
1621	Signals Network	https://coinmarketcap.com/currencies/signals-network/	0.000562101655419
1622	Italo	https://coinmarketcap.com/currencies/italo/	0.0166261953649
1623	Veros	https://coinmarketcap.com/currencies/veros/	0.0015849580996
1624	Almeela	https://coinmarketcap.com/currencies/almeela/	0.0661113889916
1625	CPUchain	https://coinmarketcap.com/currencies/cpuchain/	0.0100424614141
1626	InterCrone	https://coinmarketcap.com/currencies/intercrone/	0.00325074909013
1627	MNPCoin	https://coinmarketcap.com/currencies/mnpcoin/	0.0218056977565
1628	Origami	https://coinmarketcap.com/currencies/origami/	0.0112592369997
1629	Bulleon	https://coinmarketcap.com/currencies/bulleon/	0.0431868545941
1630	Fox Trading	https://coinmarketcap.com/currencies/fox-trading/	0.0051272021324
1631	Dragonglass	https://coinmarketcap.com/currencies/dragonglass/	0.000102323586424
1632	Jury.Online T...	https://coinmarketcap.com/currencies/jury-online-token/	0.0033240646051
1633	ConnectJob	https://coinmarketcap.com/currencies/connectjob/	0.000407513237144
1634	BEAT	https://coinmarketcap.com/currencies/beat/	0.000365254707342
1930	Pure	https://coinmarketcap.com/currencies/purex/	0.000211180387552
1635	Bettex Coin	https://coinmarketcap.com/currencies/bettex-coin/	0.00662391179715
1636	BitCoin One	https://coinmarketcap.com/currencies/bitcoin-one/	0.000477284271851
1637	Knekted	https://coinmarketcap.com/currencies/knekted/	4.49514556485e-05
1638	MarteXcoin	https://coinmarketcap.com/currencies/martexcoin/	0.012342490934
1639	ARAW	https://coinmarketcap.com/currencies/araw/	1.45091476924e-05
1640	InflationCoin	https://coinmarketcap.com/currencies/inflationcoin/	9.8154564423e-07
1641	Signatum	https://coinmarketcap.com/currencies/signatum/	0.000407150087738
1642	Aegeus	https://coinmarketcap.com/currencies/aegeus/	0.00123917435589
1643	Arqma	https://coinmarketcap.com/currencies/arqma/	0.0315130289939
1644	PlatinumBAR	https://coinmarketcap.com/currencies/platinumbar/	0.0200451168611
1645	Klimatas	https://coinmarketcap.com/currencies/klimatas/	0.0596887930186
1646	Zoomba	https://coinmarketcap.com/currencies/zoomba/	0.00207609582234
1647	ALAX	https://coinmarketcap.com/currencies/alax/	0.00204513432911
1648	CommunityGene...	https://coinmarketcap.com/currencies/communitygeneration/	0.000100729230458
1649	LOCIcoin	https://coinmarketcap.com/currencies/locicoin/	0.00101835784441
1650	EUNOMIA	https://coinmarketcap.com/currencies/eunomia/	2.53304535198e-06
1651	Skeincoin	https://coinmarketcap.com/currencies/skeincoin/	0.00302137352978
1652	Coin2.1	https://coinmarketcap.com/currencies/coin2-1/	0.000526338355304
1653	Dynamite	https://coinmarketcap.com/currencies/dynamite/	0.223038297599
1654	Waletoken	https://coinmarketcap.com/currencies/waletoken/	2.05598100706e-06
1655	P2P Global Ne...	https://coinmarketcap.com/currencies/p2p-global-network/	0.00128085854808
1656	Cryptojacks	https://coinmarketcap.com/currencies/cryptojacks/	9.90070993203e-05
1657	Shekel	https://coinmarketcap.com/currencies/shekel/	0.000301899949764
1658	PAWS Fund	https://coinmarketcap.com/currencies/paws-fund/	0.0209480347065
1659	BitRewards	https://coinmarketcap.com/currencies/bitrewards/	0.000115675743819
1660	Rupaya	https://coinmarketcap.com/currencies/rupaya/	0.000901206837821
1661	Mocrow	https://coinmarketcap.com/currencies/mocrow/	0.019242532929
1662	GoldBlocks	https://coinmarketcap.com/currencies/goldblocks/	0.00249950957065
1663	nDEX	https://coinmarketcap.com/currencies/ndex/	2.55439471007e-06
1664	Bitsum	https://coinmarketcap.com/currencies/bitsum/	2.47656971591e-05
1665	APR Coin	https://coinmarketcap.com/currencies/apr-coin/	0.00419768966255
1666	Digiwage	https://coinmarketcap.com/currencies/digiwage/	0.000805833843661
1667	Crowdholding	https://coinmarketcap.com/currencies/crowdholding/	0.000189258232977
1668	CryptoSoul	https://coinmarketcap.com/currencies/cryptosoul/	0.000232791799398
1669	Patron	https://coinmarketcap.com/currencies/patron/	9.4319067662e-05
1670	Ellaism	https://coinmarketcap.com/currencies/ellaism/	0.0019138553787
1671	ELTCOIN	https://coinmarketcap.com/currencies/eltcoin/	0.000409302720405
1672	Joint Ventures	https://coinmarketcap.com/currencies/joint-ventures/	0.00166039183051
1673	Stellar Classic	https://coinmarketcap.com/currencies/stellar-classic/	7.07935552171e-05
1674	bitJob	https://coinmarketcap.com/currencies/student-coin/	0.000408689109739
1675	BERNcash	https://coinmarketcap.com/currencies/berncash/	0.000503646152288
1676	SportyCo	https://coinmarketcap.com/currencies/sportyco/	0.000653933168867
1677	Blakecoin	https://coinmarketcap.com/currencies/blakecoin/	0.00152053336871
1678	Bata	https://coinmarketcap.com/currencies/bata/	0.0070217939952
1679	Zurcoin	https://coinmarketcap.com/currencies/zurcoin/	0.000403707748957
1680	QUINADS	https://coinmarketcap.com/currencies/quinads/	2.67075988035e-06
1681	RouletteToken	https://coinmarketcap.com/currencies/roulettetoken/	0.00342479383556
1682	Earth Token	https://coinmarketcap.com/currencies/earth-token/	0.000170297282576
1683	Innova	https://coinmarketcap.com/currencies/innova/	0.00691804733829
1684	ZINC	https://coinmarketcap.com/currencies/zinc/	0.00634212115621
1685	FundRequest	https://coinmarketcap.com/currencies/fundrequest/	0.000723856774856
1686	Arion	https://coinmarketcap.com/currencies/arion/	0.00312260614419
1687	X-Coin	https://coinmarketcap.com/currencies/x-coin/	0.00276463343845
1688	AdCoin	https://coinmarketcap.com/currencies/adcoin/	0.00211531383961
1689	Arepacoin	https://coinmarketcap.com/currencies/arepacoin/	0.00207659729062
1690	SteepCoin	https://coinmarketcap.com/currencies/steepcoin/	0.00018710212108
1691	Castle	https://coinmarketcap.com/currencies/castle/	0.00231677230053
1692	TokenDesk	https://coinmarketcap.com/currencies/tokendesk/	0.00228508388637
1693	Tracto	https://coinmarketcap.com/currencies/tracto/	0.00124336422826
1694	PluraCoin	https://coinmarketcap.com/currencies/pluracoin/	0.000100729230458
1695	KZ Cash	https://coinmarketcap.com/currencies/kz-cash/	0.021215905395
1696	Bolivarcoin	https://coinmarketcap.com/currencies/bolivarcoin/	0.00239003397836
1697	Creditbit	https://coinmarketcap.com/currencies/creditbit/	0.0019138553787
1698	Italian Lira	https://coinmarketcap.com/currencies/italian-lira/	1.38881545979e-06
1699	Open Trading ...	https://coinmarketcap.com/currencies/open-trading-network/	0.0158170064303
1700	Elementeum	https://coinmarketcap.com/currencies/elementeum/	0.0165394026988
1701	Evimeria	https://coinmarketcap.com/currencies/evimeria/	2.05063306382e-06
1702	StarterCoin	https://coinmarketcap.com/currencies/startercoin/	9.2540595055e-05
1703	Linx	https://coinmarketcap.com/currencies/linx/	0.000858212436079
1704	Absolute	https://coinmarketcap.com/currencies/absolute/	0.0024271652761
1705	Argentum	https://coinmarketcap.com/currencies/argentum/	0.00251781127482
1706	Five Star Coi...	https://coinmarketcap.com/currencies/five-star-coin-pro/	0.0141020922641
1707	WITChain	https://coinmarketcap.com/currencies/witchain/	1.62817934966e-05
1708	OP Coin	https://coinmarketcap.com/currencies/op-coin/	1.64119982792e-05
1709	BitCoen	https://coinmarketcap.com/currencies/bitcoen/	0.00431876267686
1710	Cheesecoin	https://coinmarketcap.com/currencies/cheesecoin/	8.69886936257e-05
1711	MedicCoin	https://coinmarketcap.com/currencies/mediccoin/	0.000100896737252
1712	BitRent	https://coinmarketcap.com/currencies/bitrent/	3.523e-05
1713	Dreamcoin	https://coinmarketcap.com/currencies/dreamcoin/	0.0115819318642
1714	BitStation	https://coinmarketcap.com/currencies/bitstation/	6.28208270278e-06
1715	SpreadCoin	https://coinmarketcap.com/currencies/spreadcoin/	0.00264130730442
1716	Ether Kingdom...	https://coinmarketcap.com/currencies/ether-kingdoms-token/	0.00473797530322
1717	KanadeCoin	https://coinmarketcap.com/currencies/kanadecoin/	5.33888048395e-06
1718	BoostCoin	https://coinmarketcap.com/currencies/boostcoin/	0.00244780744057
1719	SparksPay	https://coinmarketcap.com/currencies/sparkspay/	0.00524754279029
1720	Spectrum	https://coinmarketcap.com/currencies/spectrum/	2.38495856858e-05
1721	Sp8de	https://coinmarketcap.com/currencies/sp8de/	3.63584870768e-06
1722	LogisCoin	https://coinmarketcap.com/currencies/logiscoin/	0.0119568989877
1723	Scanetchain	https://coinmarketcap.com/currencies/scanetchain/	3.34859086626e-05
1724	Peony	https://coinmarketcap.com/currencies/peony/	0.0301157024044
1725	Intelligent T...	https://coinmarketcap.com/currencies/intelligent-trading-foundation/	0.00284414121411
1726	Voise	https://coinmarketcap.com/currencies/voisecom/	4.98295511835e-05
1727	Impleum	https://coinmarketcap.com/currencies/impleum/	0.00500932665675
1728	Moin	https://coinmarketcap.com/currencies/moin/	0.00312260614419
1729	Elysium	https://coinmarketcap.com/currencies/elysium/	0.00185537475979
1730	Biotron	https://coinmarketcap.com/currencies/biotron/	0.000402916921831
1731	SONDER	https://coinmarketcap.com/currencies/sonder/	0.000155656108434
1732	PayCoin	https://coinmarketcap.com/currencies/paycoin2/	0.00218917472831
1733	Payfair	https://coinmarketcap.com/currencies/payfair/	0.000729646999472
1734	FuzzBalls	https://coinmarketcap.com/currencies/fuzzballs/	0.0054266712622
1735	Qurito	https://coinmarketcap.com/currencies/qurito/	0.00251823076144
1736	Akroma	https://coinmarketcap.com/currencies/akroma/	0.0013644514959
1737	Acoin	https://coinmarketcap.com/currencies/acoin/	0.021354596857
1738	YENTEN	https://coinmarketcap.com/currencies/yenten/	0.00110136816885
1739	IQ.cash	https://coinmarketcap.com/currencies/iqcash/	0.00664812921021
1740	Peerguess	https://coinmarketcap.com/currencies/guess/	0.00042627
1741	SmartCoin	https://coinmarketcap.com/currencies/smartcoin/	0.00100712450993
1742	ShowHand	https://coinmarketcap.com/currencies/showhand/	4.1105748611e-07
1743	AmsterdamCoin	https://coinmarketcap.com/currencies/amsterdamcoin/	0.000503646152288
1744	EthereumX	https://coinmarketcap.com/currencies/ethereumx/	0.00028689667208
1745	Eurocoin	https://coinmarketcap.com/currencies/eurocoin/	0.00201458460915
1746	ParkByte	https://coinmarketcap.com/currencies/parkbyte/	0.00516998183844
1747	Garlicoin	https://coinmarketcap.com/currencies/garlicoin/	0.00054376873716
1748	Neural Protocol	https://coinmarketcap.com/currencies/neural-protocol/	2.58045890057e-06
1749	Kora Network ...	https://coinmarketcap.com/currencies/kora-network-token/	7.29646999472e-05
1750	Fivebalance	https://coinmarketcap.com/currencies/fivebalance/	4.40271226214e-05
1751	Blocklancer	https://coinmarketcap.com/currencies/blocklancer/	0.00020233396355
1752	4NEW	https://coinmarketcap.com/currencies/4new/	0.000412873424092
1753	PureVidz	https://coinmarketcap.com/currencies/purevidz/	0.000192441025025
1754	Bitcoin Adult	https://coinmarketcap.com/currencies/bitcoin-adult/	0.000703910321462
1755	InnovativeBio...	https://coinmarketcap.com/currencies/innovative-bioresearch-classic/	1.10256481559e-08
1756	Hurify	https://coinmarketcap.com/currencies/hurify/	9.7879475539e-05
1757	Cream	https://coinmarketcap.com/currencies/cream/	0.000523800947779
1758	HOdlcoin	https://coinmarketcap.com/currencies/hodlcoin/	0.000100729230458
1759	Gratz	https://coinmarketcap.com/currencies/gratz/	0.000748412298087
1760	Olympic	https://coinmarketcap.com/currencies/olympic/	0.00020192534452
1761	Onix	https://coinmarketcap.com/currencies/onix/	0.000210434489135
1762	PostCoin	https://coinmarketcap.com/currencies/postcoin/	0.00141020922641
1763	Zealium	https://coinmarketcap.com/currencies/zealium/	0.00221604307007
1764	Thingschain	https://coinmarketcap.com/currencies/thingschain/	1.92195898528e-06
1765	Tourist Token	https://coinmarketcap.com/currencies/tourist-token/	5.46341135072e-06
1766	Litecred	https://coinmarketcap.com/currencies/litecred/	0.00070997071391
1767	CDMCOIN	https://coinmarketcap.com/currencies/cdmcoin/	1.00729230458e-05
1768	Bitcoin 21	https://coinmarketcap.com/currencies/bitcoin-21/	0.0268335612715
1769	empowr coin	https://coinmarketcap.com/currencies/empowr-coin/	1.76389885182e-09
1770	CatoCoin	https://coinmarketcap.com/currencies/catocoin/	0.00171239691778
1771	Citadel	https://coinmarketcap.com/currencies/citadel/	0.0019138553787
1772	AceD	https://coinmarketcap.com/currencies/aced/	0.00886417228028
1773	Californium	https://coinmarketcap.com/currencies/californium/	0.00845275375504
1774	XDNA	https://coinmarketcap.com/currencies/xdna/	0.00483500306197
1775	Quebecoin	https://coinmarketcap.com/currencies/quebecoin/	0.0013135497117
1776	Havy	https://coinmarketcap.com/currencies/havy/	2.54767133315e-06
1777	EagleX	https://coinmarketcap.com/currencies/eaglex/	0.000604466616278
1778	EtherInc	https://coinmarketcap.com/currencies/etherinc/	6.44699825729e-05
1779	Blocknode	https://coinmarketcap.com/currencies/blocknode/	0.000104528460656
1780	Mero Currency	https://coinmarketcap.com/currencies/mero-currency/	0.00142241514546
1781	SAKECOIN	https://coinmarketcap.com/currencies/sakecoin/	4.52737150041e-06
1782	EZOOW	https://coinmarketcap.com/currencies/ezoow/	1.70100254283e-06
1783	Carebit	https://coinmarketcap.com/currencies/carebit/	0.000144886740941
1784	NevaCoin	https://coinmarketcap.com/currencies/nevacoin/	0.00483500306197
1785	Gossipcoin	https://coinmarketcap.com/currencies/gossipcoin/	0.000654739997975
1786	KWHCoin	https://coinmarketcap.com/currencies/kwhcoin/	1.06777609679e-05
1787	CyberMusic	https://coinmarketcap.com/currencies/cybermusic/	1.28133131615e-06
1788	Desire	https://coinmarketcap.com/currencies/desire/	0.00201451943234
1789	Dach Coin	https://coinmarketcap.com/currencies/dach-coin/	0.000906563074119
1790	Elliot Coin	https://coinmarketcap.com/currencies/elliot-coin/	0.000778983721089
1791	MoX	https://coinmarketcap.com/currencies/mox/	0.00364402015087
1792	BigUp	https://coinmarketcap.com/currencies/bigup/	8.5174949161e-06
1793	Ethereum Gold	https://coinmarketcap.com/currencies/ethereum-gold/	0.00151093845687
1794	Decentralized...	https://coinmarketcap.com/currencies/decentralized-asset-trading-platform/	1.5305518624e-06
1795	MojoCoin	https://coinmarketcap.com/currencies/mojocoin/	0.00144119140632
1796	Elementrem	https://coinmarketcap.com/currencies/elementrem/	0.00067162374263
1797	Octoin Coin	https://coinmarketcap.com/currencies/octoin-coin/	0.0311897255815
1798	Lightpaycoin	https://coinmarketcap.com/currencies/lightpaycoin/	0.00297087253506
1799	FidexToken	https://coinmarketcap.com/currencies/fidex-token/	5.87276853234e-07
1800	MustangCoin	https://coinmarketcap.com/currencies/mustangcoin/	0.0268483535589
1801	Bitdeal	https://coinmarketcap.com/currencies/bitdeal/	9.62580687906e-05
1802	Sola Token	https://coinmarketcap.com/currencies/sola-token/	0.000570609502795
1803	DOWCOIN	https://coinmarketcap.com/currencies/dowcoin/	0.001386329299
1804	Cyber Movie C...	https://coinmarketcap.com/currencies/cyber-movie-chain/	8.18628340872e-07
1805	Etheriya	https://coinmarketcap.com/currencies/etheriya/	0.0103317814083
1806	Natmin Pure E...	https://coinmarketcap.com/currencies/natmin-pure-escrow/	0.000164604668947
1807	Cashcoin	https://coinmarketcap.com/currencies/cashcoin/	0.000302193076463
1808	Engagement Token	https://coinmarketcap.com/currencies/engagement-token/	3.8849468457e-05
1809	X12 Coin	https://coinmarketcap.com/currencies/x12-coin/	0.00133281262762
1810	Shivers	https://coinmarketcap.com/currencies/shivers/	0.000292944559402
1811	ROIyal Coin	https://coinmarketcap.com/currencies/roiyal-coin/	0.0180305322519
1812	Zayedcoin	https://coinmarketcap.com/currencies/zayedcoin/	0.0025082949506
1813	Crystal Clear	https://coinmarketcap.com/currencies/crystal-clear/	0.00288740715201
1814	Datacoin	https://coinmarketcap.com/currencies/datacoin/	0.000402924101951
1815	HollyWoodCoin	https://coinmarketcap.com/currencies/hollywoodcoin/	0.000692638300412
1816	Micromines	https://coinmarketcap.com/currencies/micromines/	8.52603524764e-07
1817	BOAT	https://coinmarketcap.com/currencies/doubloon/	0.000206988400295
1818	AdultChain	https://coinmarketcap.com/currencies/adultchain/	0.000302187691373
1819	TajCoin	https://coinmarketcap.com/currencies/tajcoin/	0.00122866558735
1820	MASTERNET	https://coinmarketcap.com/currencies/masternet/	0.000466453021454
1821	Bionic	https://coinmarketcap.com/currencies/bionic/	2.73528643461e-05
1822	Bolenum	https://coinmarketcap.com/currencies/bolenum/	5.79205856919e-07
1823	GeyserCoin	https://coinmarketcap.com/currencies/geysercoin/	0.0130950333134
1824	Kind Ads Token	https://coinmarketcap.com/currencies/kind-ads-token/	0.000338531680202
1825	Scopuly	https://coinmarketcap.com/currencies/scopuly/	6.47281221231e-06
1826	Atheios	https://coinmarketcap.com/currencies/atheios/	0.000805833843661
1827	Joincoin	https://coinmarketcap.com/currencies/joincoin/	0.00420630484858
1828	High Voltage	https://coinmarketcap.com/currencies/high-voltage/	0.00924005475365
1829	GIGA	https://coinmarketcap.com/currencies/giga/	0.000100729230458
1830	Couchain	https://coinmarketcap.com/currencies/couchain/	3.06095751442e-06
1831	Dollarcoin	https://coinmarketcap.com/currencies/dollarcoin/	0.00143533437109
1832	SecretCoin	https://coinmarketcap.com/currencies/secretcoin/	0.0030765785201
1833	Fintab	https://coinmarketcap.com/currencies/fintab/	0.00465029236967
1834	SCRIV NETWORK	https://coinmarketcap.com/currencies/scriv-network/	0.000520757951757
1835	DeVault	https://coinmarketcap.com/currencies/devault/	0.000302187691373
1836	Independent M...	https://coinmarketcap.com/currencies/independent-money-system/	0.00232637605586
1837	Cazcoin	https://coinmarketcap.com/currencies/cazcoin/	0.000302187691373
1838	JavaScript Token	https://coinmarketcap.com/currencies/javascript-token/	0.0015586288578
1839	Phonecoin	https://coinmarketcap.com/currencies/phonecoin/	0.000111587571832
1840	BowsCoin	https://coinmarketcap.com/currencies/bowscoin/	0.00218890579303
1841	IrishCoin	https://coinmarketcap.com/currencies/irishcoin/	0.00030810804977
1842	KUN	https://coinmarketcap.com/currencies/kun/	6.02360798137
1843	Neuro	https://coinmarketcap.com/currencies/neuro/	0.000202575726046
1844	XOVBank	https://coinmarketcap.com/currencies/xovbank/	9.4320221883e-05
1845	CustomContrac...	https://coinmarketcap.com/currencies/customcontractnetwork/	8.49332659371e-06
1846	LiteBitcoin	https://coinmarketcap.com/currencies/litebitcoin/	0.000402924101951
1847	BZLCOIN	https://coinmarketcap.com/currencies/bzlcoin/	0.00535180880552
1848	SpeedCash	https://coinmarketcap.com/currencies/speedcash/	0.0202702888992
1849	e-Chat	https://coinmarketcap.com/currencies/e-chat/	0.000556385692062
1850	BumbaCoin	https://coinmarketcap.com/currencies/bumbacoin/	0.000481726595935
1851	Ccore	https://coinmarketcap.com/currencies/ccore/	0.00658578266985
1852	Paymon	https://coinmarketcap.com/currencies/paymon/	1.79984770563e-05
1853	ICOBID	https://coinmarketcap.com/currencies/icobid/	0.000101455178546
1854	SecureCoin	https://coinmarketcap.com/currencies/securecoin/	0.00100731025488
1855	PAXEX	https://coinmarketcap.com/currencies/paxex/	0.00060317369477
1856	Theresa May Coin	https://coinmarketcap.com/currencies/theresa-may-coin/	0.000104145392452
1857	Digital Money...	https://coinmarketcap.com/currencies/digital-money-bits/	0.000101077763095
1858	UltraNote Coin	https://coinmarketcap.com/currencies/ultranote-coin/	2.77112192791e-05
1859	HireGo	https://coinmarketcap.com/currencies/hirego/	0.00163839564291
1860	Nyerium	https://coinmarketcap.com/currencies/nyerium/	0.000403205087928
1861	Trident Group	https://coinmarketcap.com/currencies/trident/	0.00832594304881
1862	Cabbage	https://coinmarketcap.com/currencies/cabbage/	0.000951174628565
1863	Grimcoin	https://coinmarketcap.com/currencies/grimcoin/	0.000100731025488
1864	FUTURAX	https://coinmarketcap.com/currencies/futurax/	2.91858917793e-06
1865	Atomic Coin	https://coinmarketcap.com/currencies/atomic-coin/	0.000505772374013
1866	Project Coin	https://coinmarketcap.com/currencies/project-coin/	0.000201407435359
1867	CryptoFlow	https://coinmarketcap.com/currencies/cryptoflow/	0.000100729230458
1868	INDINODE	https://coinmarketcap.com/currencies/indinode/	1.00729230458e-05
1869	SONO	https://coinmarketcap.com/currencies/altcommunity-coin/	0.00443216512146
1870	Cryptrust	https://coinmarketcap.com/currencies/cryptrust/	1.63725668174e-06
1871	ARbit	https://coinmarketcap.com/currencies/arbit/	0.000834710806174
1872	electrumdark	https://coinmarketcap.com/currencies/electrumdark/	0.0022812477936
1873	Bitspace	https://coinmarketcap.com/currencies/bitspace/	0.000627414922033
1874	WELL	https://coinmarketcap.com/currencies/well/	9.36091155178e-05
1875	VikkyToken	https://coinmarketcap.com/currencies/vikkytoken/	2.28598138535e-06
1876	Eva Cash	https://coinmarketcap.com/currencies/eva-cash/	0.0094320221883
1877	Mero	https://coinmarketcap.com/currencies/mero/	0.00141332739791
1878	Virtacoin	https://coinmarketcap.com/currencies/virtacoin/	1.59651542864e-06
1879	BitMoney	https://coinmarketcap.com/currencies/bitmoney/	0.000100729230458
1880	Veltor	https://coinmarketcap.com/currencies/veltor/	0.0147153222809
1881	Ammo Reloaded	https://coinmarketcap.com/currencies/ammo-reloaded/	0.000103585621493
1882	Sharpe Platfo...	https://coinmarketcap.com/currencies/sharpe-platform-token/	0.000459919581091
1883	Authorship	https://coinmarketcap.com/currencies/authorship/	7.9989190724e-05
1884	Iconic	https://coinmarketcap.com/currencies/iconic/	0.013396153836
1885	Centurion	https://coinmarketcap.com/currencies/centurion/	0.000100731025488
1886	GreenMed	https://coinmarketcap.com/currencies/greenmed/	0.000515245402937
1887	Comet	https://coinmarketcap.com/currencies/comet/	0.00876359921743
1888	YoloCash	https://coinmarketcap.com/currencies/yolocash/	0.000254486636401
1889	ICOBay	https://coinmarketcap.com/currencies/icobay/	1.08062175481e-05
1890	EVOS	https://coinmarketcap.com/currencies/evos/	0.000705104613204
1891	Nekonium	https://coinmarketcap.com/currencies/nekonium/	0.000604386152926
1892	PosEx	https://coinmarketcap.com/currencies/posex/	0.00292707613988
1893	Ragnarok	https://coinmarketcap.com/currencies/ragnarok/	0.000503646152288
1894	PLNcoin	https://coinmarketcap.com/currencies/plncoin/	0.000402924101951
1895	iBTC	https://coinmarketcap.com/currencies/ibtc/	0.000181603090653
1896	Dalecoin	https://coinmarketcap.com/currencies/dalecoin/	0.00954803252616
1897	Prime-XI	https://coinmarketcap.com/currencies/prime-xi/	0.000302193076463
1898	LiteCoin Ultra	https://coinmarketcap.com/currencies/litecoin-ultra/	0.00634226977474
1899	DeltaChain	https://coinmarketcap.com/currencies/delta-chain/	8.72017145711e-07
1900	Kurrent	https://coinmarketcap.com/currencies/kurrent/	0.000103614951675
1901	Honey	https://coinmarketcap.com/currencies/honey/	0.0138327181777
1902	Escroco Emerald	https://coinmarketcap.com/currencies/escroco-emerald/	1.00731025488e-05
1903	Mirai	https://coinmarketcap.com/currencies/mirai/	0.00177925920336
1904	BunnyToken	https://coinmarketcap.com/currencies/bunnytoken/	2.49259144033e-05
1905	Traid	https://coinmarketcap.com/currencies/traid/	0.000302187691373
1906	Luna Coin	https://coinmarketcap.com/currencies/luna-coin/	0.00342485486658
1907	Wild Beast Block	https://coinmarketcap.com/currencies/wild-beast-block/	0.0318310040541
1908	Crystal Token	https://coinmarketcap.com/currencies/crystal-token/	0.0102192974021
1909	Helper Search...	https://coinmarketcap.com/currencies/helper-search-token/	6.58756309231e-07
1910	Quantis Network	https://coinmarketcap.com/currencies/quantis-network/	0.00100731025488
1911	MiloCoin	https://coinmarketcap.com/currencies/milocoin/	0.000512968277443
1912	VectorAI	https://coinmarketcap.com/currencies/vector/	0.000300278876003
1913	Bitcoin W Spe...	https://coinmarketcap.com/currencies/bitcoin-w-spectrum/	9.49760737235e-05
1914	Dinero	https://coinmarketcap.com/currencies/dinero/	0.000604386152926
1915	BrokerNekoNet...	https://coinmarketcap.com/currencies/brokernekonetwork/	1.78042245738e-06
1916	Decentralized...	https://coinmarketcap.com/currencies/decentralized-crypto-token/	5.33888048395e-06
1917	Bitvolt	https://coinmarketcap.com/currencies/bitvolt/	0.000313011468727
1918	Eternity	https://coinmarketcap.com/currencies/eternity/	0.000805848203902
1919	Xchange	https://coinmarketcap.com/currencies/xchange/	0.000508453040234
1920	Bitcoin Planet	https://coinmarketcap.com/currencies/bitcoin-planet/	0.000705117178414
1921	Alpha Coin	https://coinmarketcap.com/currencies/alpha-coin/	0.000144968811894
1922	IceChain	https://coinmarketcap.com/currencies/icechain/	6.414177643e-06
1923	Phantomx	https://coinmarketcap.com/currencies/phantomx/	0.00010051970733
1924	ICOCalendar.T...	https://coinmarketcap.com/currencies/icocalendar-today/	0.00369597142254
1925	Cannation	https://coinmarketcap.com/currencies/cannation/	0.00179756952034
1926	UralsCoin	https://coinmarketcap.com/currencies/uralscoin/	0.000299448329183
1927	CARDbuyers	https://coinmarketcap.com/currencies/cardbuyers/	0.000100731025488
1928	ZoZoCoin	https://coinmarketcap.com/currencies/zozocoin/	0.00211535153524
1931	CrevaCoin	https://coinmarketcap.com/currencies/crevacoin/	0.000100731025488
1932	Rhenium	https://coinmarketcap.com/currencies/rhenium/	0.000106920000191
1933	Coinonat	https://coinmarketcap.com/currencies/coinonat/	0.000414272246816
1934	Printex	https://coinmarketcap.com/currencies/printex/	0.000100731025488
1935	VIVO	https://coinmarketcap.com/currencies/vivo/	0.000705117178414
1936	SocialCoin	https://coinmarketcap.com/currencies/socialcoin-socc/	0.000315610375797
1937	FolmCoin	https://coinmarketcap.com/currencies/folmcoin/	0.000302193076463
1938	Simmitri	https://coinmarketcap.com/currencies/simmitri/	4.02924101951e-05
1939	Levocoin	https://coinmarketcap.com/currencies/levocoin/	0.000103591237098
1940	PonziCoin	https://coinmarketcap.com/currencies/ponzicoin/	0.00322339281561
1941	CFun	https://coinmarketcap.com/currencies/cfun/	6.10212960956e-06
1942	Qbic	https://coinmarketcap.com/currencies/qbic/	0.000556755841919
1943	Ethereum Meta	https://coinmarketcap.com/currencies/ethereum-meta/	4.20631190926e-05
1944	Provoco Token	https://coinmarketcap.com/currencies/provoco-token/	6.40126314942e-06
1945	GambleCoin	https://coinmarketcap.com/currencies/gamblecoin/	0.000214367553752
1946	BitCoal	https://coinmarketcap.com/currencies/bitcoal/	0.000505710070721
1947	AnarchistsPrime	https://coinmarketcap.com/currencies/anarchistsprime/	0.000503655127439
1948	Dystem	https://coinmarketcap.com/currencies/dystem/	0.000312710243341
1949	Cointorox	https://coinmarketcap.com/currencies/cointorox/	0.000373721633876
1950	BenjiRolls	https://coinmarketcap.com/currencies/benjirolls/	0.000101334486446
1951	LRM Coin	https://coinmarketcap.com/currencies/lrm-coin/	0.000203749827427
1952	CoinonatX	https://coinmarketcap.com/currencies/coinonatx/	0.000100437370544
1953	QYNO	https://coinmarketcap.com/currencies/qyno/	0.00181315845878
1954	LitecoinToken	https://coinmarketcap.com/currencies/litecoin-token/	2.00714881376e-08
1955	Project-X	https://coinmarketcap.com/currencies/project-x/	22982.8915063
1956	Staker	https://coinmarketcap.com/currencies/staker/	0.00120963720405
1957	Oceanlab	https://coinmarketcap.com/currencies/oceanlab/	3.79824236955e-05
1958	SpectrumNetwork	https://coinmarketcap.com/currencies/spectrum-network/	1.77962682798e-06
1959	BROTHER	https://coinmarketcap.com/currencies/brat/	1e-05
1960	Claymore	https://coinmarketcap.com/currencies/claymore/	4.65027879117e-05
1961	Eryllium	https://coinmarketcap.com/currencies/eryllium/	0.000100731025488
1962	Save and Gain	https://coinmarketcap.com/currencies/save-and-gain/	0.000377519320519
1963	Concoin	https://coinmarketcap.com/currencies/concoin/	0.00143841386671
1964	Magnum	https://coinmarketcap.com/currencies/magnum/	0.000207325881912
1965	Graphcoin	https://coinmarketcap.com/currencies/graphcoin/	0.000108815604833
1966	Abulaba	https://coinmarketcap.com/currencies/abulaba/	4.88913132973e-05
1967	Bitcoinus	https://coinmarketcap.com/currencies/bitcoinus/	1.16806143121e-05
1968	Posscoin	https://coinmarketcap.com/currencies/posscoin/	1.77927222305e-08
1969	Interzone	https://coinmarketcap.com/currencies/interzone/	0.000201462050975
1970	dietbitcoin	https://coinmarketcap.com/currencies/dietbitcoin/	0.000178021881378
1971	Benz	https://coinmarketcap.com/currencies/benz/	8.64090128507e-05
1972	PlayerCoin	https://coinmarketcap.com/currencies/playercoin/	1.21625290467e-05
1973	Azart	https://coinmarketcap.com/currencies/azart/	0.000100731025488
1974	SmartFox	https://coinmarketcap.com/currencies/smartfox/	0.000192740613779
1975	StellarPay	https://coinmarketcap.com/currencies/stellarpay/	8.23064223183e-05
1976	MFIT COIN	https://coinmarketcap.com/currencies/mfit-coin/	0.000122780650937
1977	SongCoin	https://coinmarketcap.com/currencies/songcoin/	7.22525047279e-06
1978	Argus	https://coinmarketcap.com/currencies/argus/	0.000201462050975
1979	HarmonyCoin	https://coinmarketcap.com/currencies/harmonycoin-hmc/	0.000402924101951
1980	Blacer Coin	https://coinmarketcap.com/currencies/blacer-coin/	0.00116224489359
1981	Bitcoin X	https://coinmarketcap.com/currencies/bitcoin-x/	4.76201443412e-05
1982	Jiyo [OLD]	https://coinmarketcap.com/currencies/jiyo-old/	2.05106397294e-05
1983	Ourcoin	https://coinmarketcap.com/currencies/ourcoin/	0.000201462050975
1984	CK USD	https://coinmarketcap.com/currencies/ckusd/	0.258716256826
1985	Molecular Future	https://coinmarketcap.com/currencies/molecular-future/	0.621070904012
1986	Eminer	https://coinmarketcap.com/currencies/eminer/	0.0416610670714
1987	Pledge Coin	https://coinmarketcap.com/currencies/pledge-coin/	0.00503164106637
1988	En-Tan-Mo	https://coinmarketcap.com/currencies/en-tan-mo/	0.145180682313
1989	Super Zero	https://coinmarketcap.com/currencies/super-zero/	0.138190053242
1990	DigiFinexToken	https://coinmarketcap.com/currencies/digifinextoken/	0.815871085944
1991	BitMax Token	https://coinmarketcap.com/currencies/bitmax-token/	0.0907416111748
1992	FOIN	https://coinmarketcap.com/currencies/foin/	1549.63624172
1993	Filecoin [Fut...	https://coinmarketcap.com/currencies/filecoin/	3.53088349008
1994	Ontology Gas	https://coinmarketcap.com/currencies/ontology-gas/	0.169311480513
1995	YOU COIN	https://coinmarketcap.com/currencies/you-coin/	0.0771164046079
1996	V-Dimension	https://coinmarketcap.com/currencies/v-dimension/	1.42381952572
1997	Gatechain Token	https://coinmarketcap.com/currencies/gatechain-token/	0.712450780879
1998	MINDOL	https://coinmarketcap.com/currencies/mindol/	0.22819399317
1999	Coni	https://coinmarketcap.com/currencies/coni/	0.0218307688557
2000	YottaChain	https://coinmarketcap.com/currencies/yottachain/	0.0814987905623
2001	WinToken	https://coinmarketcap.com/currencies/wintoken/	0.00133501301891
2002	Wirex Token	https://coinmarketcap.com/currencies/wirex-token/	0.0160534474041
2003	FairGame	https://coinmarketcap.com/currencies/fairgame/	0.00438606047085
2004	VinDax Coin	https://coinmarketcap.com/currencies/vindax-coin/	0.055258877311
2005	Bilaxy Token	https://coinmarketcap.com/currencies/bilaxy-token/	0.00619992511804
2006	EMOGI Network	https://coinmarketcap.com/currencies/emogi-network/	0.00481916225082
2007	StarChain	https://coinmarketcap.com/currencies/starchain/	0.00699540964369
2008	BUMO	https://coinmarketcap.com/currencies/bumo/	0.0151211598676
2009	Amino Network	https://coinmarketcap.com/currencies/amino-network/	0.172274831945
2010	VIDY	https://coinmarketcap.com/currencies/vidy/	0.0022355273742
2011	RSK Smart Bit...	https://coinmarketcap.com/currencies/rsk-smart-bitcoin/	10044.0186358
2012	LightChain	https://coinmarketcap.com/currencies/lightchain/	1.93049735721e-05
2013	VideoCoin	https://coinmarketcap.com/currencies/videocoin/	0.346652598148
2014	Nestree	https://coinmarketcap.com/currencies/nestree/	0.00428192612875
2015	PLANET	https://coinmarketcap.com/currencies/planet/	0.1748621973
2016	CoinEx Token	https://coinmarketcap.com/currencies/coinex-token/	0.015680911127
2017	Aidos Kuneen	https://coinmarketcap.com/currencies/aidos-kuneen/	4.83242201577
2018	BitForex Token	https://coinmarketcap.com/currencies/bitforex-token/	0.0124042909915
2019	Defi	https://coinmarketcap.com/currencies/defi/	0.0779658559071
2020	NSS Coin	https://coinmarketcap.com/currencies/nss-coin/	0.123252285044
2021	Terra	https://coinmarketcap.com/currencies/terra/	1.06147267021
2022	Swipe	https://coinmarketcap.com/currencies/swipe/	0.354619940647
2023	ShineChain	https://coinmarketcap.com/currencies/shinechain/	0.00133933585365
2024	Huobi Pool Token	https://coinmarketcap.com/currencies/huobi-pool-token/	0.00931951213413
2025	DREP	https://coinmarketcap.com/currencies/drep/	0.00314666898651
2026	Dapp Token	https://coinmarketcap.com/currencies/dapp-token/	0.00270980272565
2027	OceanEx Token	https://coinmarketcap.com/currencies/oceanex-token/	0.0036257991808
2028	CONUN	https://coinmarketcap.com/currencies/conun/	0.00777935928946
2029	Ferrum Network	https://coinmarketcap.com/currencies/ferrum-network/	0.00644480056746
2030	MixMarvel	https://coinmarketcap.com/currencies/mixmarvel/	0.0543946347047
2031	B91	https://coinmarketcap.com/currencies/b91/	0.028874083183
2032	Polkadot [IOU]	https://coinmarketcap.com/currencies/polkadot-iou/	146.347376774
2033	InvestDigital	https://coinmarketcap.com/currencies/investdigital/	0.0211889997931
2034	PlayCoin [QRC20]	https://coinmarketcap.com/currencies/playcoin/	0.00875077637803
2035	FNB Protocol	https://coinmarketcap.com/currencies/fnb-protocol/	0.113610990985
2036	DEXTER	https://coinmarketcap.com/currencies/dexter/	381.16224135
2037	KNOW	https://coinmarketcap.com/currencies/know/	0.00153343177278
2038	DeepCloud AI	https://coinmarketcap.com/currencies/deepcloud-ai/	0.01895355784
2039	Tratok	https://coinmarketcap.com/currencies/tratok/	0.00398354337572
2040	GlitzKoin	https://coinmarketcap.com/currencies/glitzkoin/	0.179699272231
2041	Yobit Token	https://coinmarketcap.com/currencies/yobit-token/	1196.26334374
2042	QuickX Protocol	https://coinmarketcap.com/currencies/quickx-protocol/	0.0249775869798
2043	Blockcloud	https://coinmarketcap.com/currencies/blockcloud/	0.00447181672651
2044	DUO Network T...	https://coinmarketcap.com/currencies/duo-network-token/	0.103472001499
2045	VeThor Token	https://coinmarketcap.com/currencies/vethor-token/	0.000610727511223
2046	CNNS	https://coinmarketcap.com/currencies/cnns/	0.00759269736535
2047	ARPA Chain	https://coinmarketcap.com/currencies/arpa-chain/	0.0145357961839
2048	Electronic En...	https://coinmarketcap.com/currencies/electronic-energy-coin/	0.0239924436615
2049	Promotion Coin	https://coinmarketcap.com/currencies/promotion-coin/	0.000594427132189
2050	Exchange Union	https://coinmarketcap.com/currencies/exchange-union/	1.19738982082
2051	Dexter G	https://coinmarketcap.com/currencies/dexter-g/	0.730421035187
2052	Engine	https://coinmarketcap.com/currencies/engine/	0.000804118503705
2053	Bitcloud Pro	https://coinmarketcap.com/currencies/bitcloud-pro/	0.0211795712022
2054	12Ships	https://coinmarketcap.com/currencies/12ships/	0.0323202945482
2055	MyToken	https://coinmarketcap.com/currencies/mytoken/	0.00188501092511
2056	WHEN Token	https://coinmarketcap.com/currencies/when-token/	0.00511484775343
2057	Asgard	https://coinmarketcap.com/currencies/asgard/	0.00207961478162
2058	OFCOIN	https://coinmarketcap.com/currencies/ofcoin/	0.000125002503799
2059	Ladder Networ...	https://coinmarketcap.com/currencies/ladder-network-token/	0.0681067798116
2060	Yuan Chain Coin	https://coinmarketcap.com/currencies/yuan-chain-coin/	0.00939850752087
2061	TCOIN	https://coinmarketcap.com/currencies/tcoin/	0.0224630186838
2062	Tokoin	https://coinmarketcap.com/currencies/tokoin/	0.142861674518
2063	LinkToken	https://coinmarketcap.com/currencies/linktoken/	0.0493371847808
2064	DIPNET	https://coinmarketcap.com/currencies/dipnet/	0.000473594426243
2065	Gosama	https://coinmarketcap.com/currencies/gosama/	0.14045574724
2066	USDCoin	https://coinmarketcap.com/currencies/usdcoin/	1.00342647269
2067	Webflix Token	https://coinmarketcap.com/currencies/webflix-token/	0.000765555793707
2068	Volume Network	https://coinmarketcap.com/currencies/volume-network/	0.0595604667828
2069	Taklimakan Ne...	https://coinmarketcap.com/currencies/taklimakan-network/	0.00553648179236
2070	ZeuxCoin	https://coinmarketcap.com/currencies/zeuxcoin/	0.0257704181296
2071	Sparkle	https://coinmarketcap.com/currencies/sparkle/	0.0430935700701
2072	TopChain	https://coinmarketcap.com/currencies/topchain/	0.0106704224148
2073	SoPay	https://coinmarketcap.com/currencies/sopay/	0.000562542039049
2074	Ubique Chain ...	https://coinmarketcap.com/currencies/ubique-chain-of-things/	0.0181343528654
2075	BORA	https://coinmarketcap.com/currencies/bora/	0.0159375877332
2076	Alphacon	https://coinmarketcap.com/currencies/alphacon/	0.0069587061152
2077	M2O	https://coinmarketcap.com/currencies/m2o/	0.00116241785352
2078	FIBOS	https://coinmarketcap.com/currencies/fibos/	0.0117350481241
2079	Blockchain Qu...	https://coinmarketcap.com/currencies/blockchain-quotations-index-token/	0.0141420925469
2080	Wavesbet	https://coinmarketcap.com/currencies/wavesbet/	9.34361355865e-06
2081	ThingsOperati...	https://coinmarketcap.com/currencies/thingsoperatingsystem/	0.00238400581577
2082	Influence Chain	https://coinmarketcap.com/currencies/influence-chain/	0.00274308493857
2083	Game Stars	https://coinmarketcap.com/currencies/game-stars/	0.000505103565439
2084	PalletOne	https://coinmarketcap.com/currencies/palletone/	0.00696568031518
2085	Futurepia	https://coinmarketcap.com/currencies/futurepia/	0.00642376422623
2086	YouLive Coin	https://coinmarketcap.com/currencies/youlive-coin/	0.000463235546088
2087	bitCEO	https://coinmarketcap.com/currencies/bitceo/	0.133346520368
2088	BidiPass	https://coinmarketcap.com/currencies/bidipass/	0.0603164377438
2089	Emirex Token	https://coinmarketcap.com/currencies/emirex-token/	0.0386807137873
2090	Magic Cube Coin	https://coinmarketcap.com/currencies/magic-cube-coin/	0.00287344283611
2091	Simone	https://coinmarketcap.com/currencies/simone/	702.825067676
2092	PATHHIVE	https://coinmarketcap.com/currencies/phv/	0.0263485512749
2093	EveriToken	https://coinmarketcap.com/currencies/everitoken/	0.0343210094614
2094	IOU	https://coinmarketcap.com/currencies/iou/	0.233978242278
2095	BOOM	https://coinmarketcap.com/currencies/boom/	0.00244271435125
2096	Baer Chain	https://coinmarketcap.com/currencies/baer-chain/	2.13672950365
2097	HitChain	https://coinmarketcap.com/currencies/hitchain/	7.82455179321e-05
2098	BitcoinX	https://coinmarketcap.com/currencies/bitcoinx/	0.00115704197597
2099	Netbox Coin	https://coinmarketcap.com/currencies/netbox-coin/	0.037063898589
2100	Smartup	https://coinmarketcap.com/currencies/smartup/	0.000975639535515
2101	CHEX	https://coinmarketcap.com/currencies/chex/	0.0126558552519
2102	BitUP Token	https://coinmarketcap.com/currencies/bitup-token/	0.00355724556607
2103	Opennity	https://coinmarketcap.com/currencies/opennity/	0.000636192203732
2104	Monarch	https://coinmarketcap.com/currencies/monarch/	0.00610490972579
2105	CoinMeet	https://coinmarketcap.com/currencies/coinmeet/	0.0107128479276
2106	WETH	https://coinmarketcap.com/currencies/weth/	160.334501584
2107	KEY	https://coinmarketcap.com/currencies/key/	0.00136048282783
2108	Coindom	https://coinmarketcap.com/currencies/coindom/	0.00303248411488
2109	CryptoBonusMiles	https://coinmarketcap.com/currencies/cryptobonusmiles/	0.000174569920452
2110	Krypton Galax...	https://coinmarketcap.com/currencies/krypton-galaxy-coin/	0.00343656115883
2111	Boltt Coin	https://coinmarketcap.com/currencies/boltt-coin/	0.0630349626808
2112	Intelligent I...	https://coinmarketcap.com/currencies/intelligent-investment-chain/	0.000267400522019
2113	EduCoin	https://coinmarketcap.com/currencies/edu-coin/	0.000211318974012
2114	Bitcoin BEP2	https://coinmarketcap.com/currencies/bitcoin-bep2/	10056.0923933
2115	BeeKan	https://coinmarketcap.com/currencies/beekan/	0.000497728674894
2116	Lukki Operati...	https://coinmarketcap.com/currencies/lukki-operating-token/	0.00917277257642
2117	NNB Token	https://coinmarketcap.com/currencies/nnb-token/	0.00234753950373
2118	InsurChain	https://coinmarketcap.com/currencies/insurchain/	0.000231499455195
2119	Experience Token	https://coinmarketcap.com/currencies/experience-token/	0.000153279931432
2120	Super Bitcoin	https://coinmarketcap.com/currencies/super-bitcoin/	2.6320251371
2121	Consentium	https://coinmarketcap.com/currencies/consentium/	0.100709407302
2122	xCrypt Token	https://coinmarketcap.com/currencies/xcrypt-token/	0.00278396103129
2123	Cybereits	https://coinmarketcap.com/currencies/cybereits/	0.00206452955065
2124	IZIChain	https://coinmarketcap.com/currencies/izichain/	0.20833963191
2125	Themis	https://coinmarketcap.com/currencies/themis/	0.00550715357743
2126	Globalvillage...	https://coinmarketcap.com/currencies/globalvillage-ecosystem/	0.000422843023896
2127	SPIN Protocol	https://coinmarketcap.com/currencies/spin-protocol/	0.00549667293993
2128	Esports Token	https://coinmarketcap.com/currencies/esports-token/	0.000662021180009
2129	United Bitcoin	https://coinmarketcap.com/currencies/united-bitcoin/	0.778362764948
2130	Show	https://coinmarketcap.com/currencies/show/	0.000921863133392
2131	T.OS	https://coinmarketcap.com/currencies/t-os/	0.0128460732736
2132	FundToken	https://coinmarketcap.com/currencies/fundtoken/	0.00654739997975
2133	FuturoCoin	https://coinmarketcap.com/currencies/futurocoin/	0.409385442639
2134	Endorsit	https://coinmarketcap.com/currencies/endorsit/	8.31726810774e-05
2135	MSD	https://coinmarketcap.com/currencies/msd/	0.00523811943732
2136	MineBee	https://coinmarketcap.com/currencies/minebee/	0.119321094355
2137	xEURO	https://coinmarketcap.com/currencies/xeuro/	1.09503440459
2138	Bitex Global ...	https://coinmarketcap.com/currencies/bitex-global-xbx-coin/	0.00718215169812
2139	CarBlock	https://coinmarketcap.com/currencies/carblock/	0.00101972617243
2140	MGC Token	https://coinmarketcap.com/currencies/mgc-token/	0.0472524277795
2141	FLETA	https://coinmarketcap.com/currencies/fleta/	0.0115428995102
2142	Muzika	https://coinmarketcap.com/currencies/muzika/	0.00648930338773
2143	Digital Fanta...	https://coinmarketcap.com/currencies/digital-fantasy-sports/	0.0794740574623
2144	Helpico	https://coinmarketcap.com/currencies/helpico/	13.3278003252
2145	Zerobank	https://coinmarketcap.com/currencies/zerobank/	0.01661714273
2146	Maggie	https://coinmarketcap.com/currencies/maggie/	0.000530843044512
2147	Agoras Tokens	https://coinmarketcap.com/currencies/agoras-tokens/	0.23238975177
2148	Diruna	https://coinmarketcap.com/currencies/diruna/	0.000883890846986
2149	CARAT	https://coinmarketcap.com/currencies/carat/	0.491693156355
2150	Bitcoin File	https://coinmarketcap.com/currencies/bitcoin-file/	0.00372145185811
2151	Marginless	https://coinmarketcap.com/currencies/marginless/	2.24061279362e-05
2152	SEER	https://coinmarketcap.com/currencies/seer/	0.000450779384533
2153	ioeX	https://coinmarketcap.com/currencies/ioex/	0.0309427209871
2154	vSportCoin	https://coinmarketcap.com/currencies/vsportcoin/	0.00101452458235
2155	Livepeer	https://coinmarketcap.com/currencies/livepeer/	5.0051278969
2156	Brazilian Dig...	https://coinmarketcap.com/currencies/brz/	0.243764737708
2157	Emanate	https://coinmarketcap.com/currencies/emanate/	0.0283322862367
2158	MEX	https://coinmarketcap.com/currencies/mex/	0.000985755412594
2159	BUDDY	https://coinmarketcap.com/currencies/buddy/	2.12874887347e-05
2160	Big Bang Game...	https://coinmarketcap.com/currencies/big-bang-game-coin/	0.00032600086842
2161	HOT Token	https://coinmarketcap.com/currencies/hot-token/	0.00203587742354
2162	Uranus	https://coinmarketcap.com/currencies/uranus/	0.00130885884936
2163	Binance GBP S...	https://coinmarketcap.com/currencies/binance-gbp-stable-coin/	1.24601176643
2164	Pixie Coin	https://coinmarketcap.com/currencies/pixie-coin/	0.000684990793958
2165	Social Lendin...	https://coinmarketcap.com/currencies/social-lending-token/	0.00244349941867
2166	Atlas Token	https://coinmarketcap.com/currencies/atlas-token/	0.0162818058492
2167	PDATA	https://coinmarketcap.com/currencies/pdata/	0.00311253322114
2168	MediBit	https://coinmarketcap.com/currencies/medibit/	4.07534461504e-06
2169	Hintchain	https://coinmarketcap.com/currencies/hintchain/	0.0191338296489
2170	Hero	https://coinmarketcap.com/currencies/hero/	0.0431632159961
2171	Celsius	https://coinmarketcap.com/currencies/celsius/	0.0592750370056
2172	SDUSD	https://coinmarketcap.com/currencies/sdusd/	0.924892469332
2173	CapdaxToken	https://coinmarketcap.com/currencies/capdaxtoken/	0.00291860579416
2174	Hdac	https://coinmarketcap.com/currencies/hdac/	0.0170168415116
2175	CENTERCOIN	https://coinmarketcap.com/currencies/centercoin/	0.00409868408947
2176	DACC	https://coinmarketcap.com/currencies/dacc/	0.000101692507407
2177	Custody Token	https://coinmarketcap.com/currencies/custody-token/	0.00395577837044
2178	Read	https://coinmarketcap.com/currencies/read/	0.0026189599919
2179	CryptoFranc	https://coinmarketcap.com/currencies/cryptofranc/	1.00875999931
2180	Sparkster	https://coinmarketcap.com/currencies/sparkster/	0.00335637619757
2181	Xenoverse	https://coinmarketcap.com/currencies/xenoverse/	0.000991844277911
2182	WEBN token	https://coinmarketcap.com/currencies/webn-token/	6.05073121514e-06
2183	VENJOCOIN	https://coinmarketcap.com/currencies/venjocoin/	6.10419136574
2184	KingXChain	https://coinmarketcap.com/currencies/kingxchain/	1.40590519411e-06
2185	Qube	https://coinmarketcap.com/currencies/qube/	0.000601474833959
2186	GSENetwork	https://coinmarketcap.com/currencies/gsenetwork/	0.000109326238012
2187	NOIZchain	https://coinmarketcap.com/currencies/noizchain/	0.491961561555
2188	Airline & Lif...	https://coinmarketcap.com/currencies/airline-and-life-networking-token/	0.181004686887
2189	CariNet	https://coinmarketcap.com/currencies/carinet/	0.00311790620262
2190	Aunite	https://coinmarketcap.com/currencies/aunite/	0.0259676246001
2191	BlockCDN	https://coinmarketcap.com/currencies/blockcdn/	0.0034455784093
2192	Twinkle	https://coinmarketcap.com/currencies/twinkle/	0.00251823076144
2193	Countinghouse	https://coinmarketcap.com/currencies/countinghouse/	1.20154393337
2194	Infinitecoin	https://coinmarketcap.com/currencies/infinitecoin/	1.4099743139e-05
2195	NPCoin	https://coinmarketcap.com/currencies/npcoin/	0.00674885844066
2196	OTCBTC Token	https://coinmarketcap.com/currencies/otcbtc-token/	0.0111711117785
2197	Carlive Chain	https://coinmarketcap.com/currencies/carlive-chain/	0.000171591618754
2198	The Midas Tou...	https://coinmarketcap.com/currencies/the-midas-touch-gold/	0.00106028579313
2199	TranslateMe N...	https://coinmarketcap.com/currencies/translateme-network-token/	0.000827980404079
2200	IDEALCOIN	https://coinmarketcap.com/currencies/idealcoin/	0.030315348863
2201	Monero Classic	https://coinmarketcap.com/currencies/monero-classic/	0.343373241436
2202	GoldFund	https://coinmarketcap.com/currencies/goldfund/	0.000405876851829
2203	COMSA [XEM]	https://coinmarketcap.com/currencies/comsa-xem/	0.0663566927453
2204	Usechain Token	https://coinmarketcap.com/currencies/usechain-token/	0.00115162412075
2205	DECOIN	https://coinmarketcap.com/currencies/decoin/	0.0303786443884
2206	Ti-Value	https://coinmarketcap.com/currencies/ti-value/	0.0179188669131
2207	COMSA [ETH]	https://coinmarketcap.com/currencies/comsa-eth/	0.0666391906691
2208	Jingtum Tech	https://coinmarketcap.com/currencies/jingtum-tech/	0.000619903189796
2209	1X2 COIN	https://coinmarketcap.com/currencies/1x2-coin/	0.074822038294
2210	Dragon Token	https://coinmarketcap.com/currencies/dragon-token/	3.73456509346
2211	Commerce Data...	https://coinmarketcap.com/currencies/commerce-data-connection/	0.000163672951559
2212	Hyper Pay	https://coinmarketcap.com/currencies/hyper-pay/	0.00143440382105
2213	Agrocoin	https://coinmarketcap.com/currencies/agrocoin/	5.85618867893
2214	BuckHathCoin	https://coinmarketcap.com/currencies/buck-hath-coin/	0.0241852862856
2215	QUSD	https://coinmarketcap.com/currencies/qusd/	0.0137765817294
2216	Infinity Econ...	https://coinmarketcap.com/currencies/infinity-economics/	0.00204852077621
2217	Jinbi Token	https://coinmarketcap.com/currencies/jinbi-token/	12.4988502946
2218	Future1coin	https://coinmarketcap.com/currencies/future1coin/	0.00323118858331
2219	Volt	https://coinmarketcap.com/currencies/volt/	9.96007331364e-05
2220	ROMToken	https://coinmarketcap.com/currencies/romtoken/	0.000142701300805
2221	Xtock	https://coinmarketcap.com/currencies/xtock/	0.000637958756541
2222	NewsToken	https://coinmarketcap.com/currencies/newstoken/	0.000222181381203
2223	LemoChain	https://coinmarketcap.com/currencies/lemochain/	0.00400690904758
2224	Golden Token	https://coinmarketcap.com/currencies/golden-token/	0.0259153583709
2225	Stellar Gold	https://coinmarketcap.com/currencies/stellar-gold/	0.00351448098036
2226	Bitcoin God	https://coinmarketcap.com/currencies/bitcoin-god/	8.12076763844
2227	Merebel	https://coinmarketcap.com/currencies/merebel/	0.213060414672
2228	SuperEdge	https://coinmarketcap.com/currencies/superedge/	2.89890002995e-05
2229	Asura Coin	https://coinmarketcap.com/currencies/asura-coin/	0.000137031265755
2230	ORS Group	https://coinmarketcap.com/currencies/ors-group/	0.0221167218238
2231	Maya Preferre...	https://coinmarketcap.com/currencies/maya-preferred-223/	407.106574079
2232	Thar Token	https://coinmarketcap.com/currencies/thar-token/	0.0947916509511
2233	ClubCoin	https://coinmarketcap.com/currencies/clubcoin/	0.0580200367436
2234	Mobile Crypto...	https://coinmarketcap.com/currencies/mobile-crypto-pay-coin/	0.00795542951501
2235	ETHplode	https://coinmarketcap.com/currencies/ethplode/	0.00520144338721
2236	StockChain	https://coinmarketcap.com/currencies/stockchain/	0.000111507258117
2237	Pabyosi Coin ...	https://coinmarketcap.com/currencies/pabyosi-coin-special/	0.0259881414581
2238	Blockium	https://coinmarketcap.com/currencies/blockium/	0.00300173106764
2239	HoryouToken	https://coinmarketcap.com/currencies/horyoutoken/	0.00201523782071
2240	EncryptoTel [...	https://coinmarketcap.com/currencies/encryptotel-eth/	0.00493573229243
2241	WINCOIN	https://coinmarketcap.com/currencies/win-coin/	0.0304202275982
2242	Sexcoin	https://coinmarketcap.com/currencies/sexcoin/	0.00302137352978
2243	TerraNova	https://coinmarketcap.com/currencies/terranova/	0.0270961629931
2244	Crypto Harbor...	https://coinmarketcap.com/currencies/crypto-harbor-exchange/	3.16684361599e-05
2245	First Bitcoin	https://coinmarketcap.com/currencies/first-bitcoin/	0.00866271381936
2246	GOLD Reward T...	https://coinmarketcap.com/currencies/gold-reward-token/	0.00161166768732
2247	InnovaMinex	https://coinmarketcap.com/currencies/innovaminex/	0.0805670433526
2248	MobilinkToken	https://coinmarketcap.com/currencies/mobilinktoken/	0.00144148651023
2249	Wiki Token	https://coinmarketcap.com/currencies/wiki-token/	0.57980939003
2250	NAM COIN	https://coinmarketcap.com/currencies/nam-coin/	5.03646152288e-05
2251	Zenon	https://coinmarketcap.com/currencies/zenon/	1.41020922641
2252	Gamblica	https://coinmarketcap.com/currencies/gamblica/	7.11850731193e-05
2253	Bidooh DOOH T...	https://coinmarketcap.com/currencies/bidooh-dooh-token/	3.55777252181e-05
2254	LevelApp Token	https://coinmarketcap.com/currencies/levelapp-token/	0.000132378328649
2255	Tronipay	https://coinmarketcap.com/currencies/tronipay/	0.0138063023648
2256	ShopZcoin	https://coinmarketcap.com/currencies/shopzcoin/	0.000604375382746
2257	WeToken	https://coinmarketcap.com/currencies/wetoken/	0.000100729230458
2258	PlusOneCoin	https://coinmarketcap.com/currencies/plusonecoin/	0.0354783651231
2259	Oculor	https://coinmarketcap.com/currencies/oculor/	1.87057664267e-05
2260	Content and A...	https://coinmarketcap.com/currencies/content-and-ad-network/	0.000189582043481
2261	Bubble	https://coinmarketcap.com/currencies/bubble/	0.00684958767112
2262	Valuto	https://coinmarketcap.com/currencies/valuto/	0.00120875076549
2263	Blockmason Link	https://coinmarketcap.com/currencies/blockmason-link/	0.000505430194578
2264	BTCMoon	https://coinmarketcap.com/currencies/btcmoon/	0.00141020922641
2265	MoneroV	https://coinmarketcap.com/currencies/monero-v/	0.00480614003132
2266	Quotient	https://coinmarketcap.com/currencies/quotient/	0.000201458460915
2267	TRUNK COIN	https://coinmarketcap.com/currencies/trunk-coin/	0.000503646152288
2268	CottonCoin	https://coinmarketcap.com/currencies/cottoncoin/	0.00292114768327
2269	Hilux	https://coinmarketcap.com/currencies/hilux/	0.00493573229243
2270	Tellurion	https://coinmarketcap.com/currencies/tellurion/	0.000302187691373
2271	GazeCoin	https://coinmarketcap.com/currencies/gazecoin/	0.00433135690968
2272	SaveNode	https://coinmarketcap.com/currencies/savenode/	0.000300511271987
2273	OOOBTC TOKEN	https://coinmarketcap.com/currencies/ooobtc-token/	0.00231677230053
2274	Minex	https://coinmarketcap.com/currencies/minex/	0.00201458460915
2275	DWS	https://coinmarketcap.com/currencies/dws/	0.000522520496968
2276	Ethereum Lite	https://coinmarketcap.com/currencies/ethereum-lite/	0.00493573229243
2277	Infinipay	https://coinmarketcap.com/currencies/infinipay/	0.000120875076549
2278	Concierge Coin	https://coinmarketcap.com/currencies/concierge-coin/	0.000302187691373
2279	SpectrumCash	https://coinmarketcap.com/currencies/spectrumcash/	0.000100632919776
2280	MESSE TOKEN	https://coinmarketcap.com/currencies/messe-token/	0.0019242532929
2281	Halloween Coin	https://coinmarketcap.com/currencies/halloween-coin/	2.02584783405e-05
2282	One DEX	https://coinmarketcap.com/currencies/one-dex/	3.21339288207e-07
2283	ERA	https://coinmarketcap.com/currencies/blakestar/	0.0002680205377
2284	PROUD Money	https://coinmarketcap.com/currencies/proud-money/	0.00120875076549
2285	SealBlock Token	https://coinmarketcap.com/currencies/sealblock-token/	8.89813413991e-06
2286	BIZKEY	https://coinmarketcap.com/currencies/bizkey/	0.000204657085218
2287	CMITCOIN	https://coinmarketcap.com/currencies/cmitcoin/	5.33888048395e-06
2288	HondaisCoin	https://coinmarketcap.com/currencies/hondaiscoin/	1.00729230458e-05
2289	Excaliburcoin	https://coinmarketcap.com/currencies/excaliburcoin/	6.19839413873e-06
2290	Bastonet	https://coinmarketcap.com/currencies/bastonet/	6.82896644131e-07
2291	eosBLACK	https://coinmarketcap.com/currencies/eosblack/	0.00199318204734
2292	BetaCoin	https://coinmarketcap.com/currencies/betacoin/	0.00161334952932
2293	RabbitCoin	https://coinmarketcap.com/currencies/rabbitcoin/	1.43e-06
2294	Axiom	https://coinmarketcap.com/currencies/axiom/	0.00593119651412
2295	AvatarCoin	https://coinmarketcap.com/currencies/avatarcoin/	0.0742151064182
2296	Francs	https://coinmarketcap.com/currencies/francs/	0.00831061993098
2297	Aces	https://coinmarketcap.com/currencies/aces/	0.000123741847099
2298	DynamicCoin	https://coinmarketcap.com/currencies/dynamiccoin/	9.44701401219e-05
2299	BlazerCoin	https://coinmarketcap.com/currencies/blazercoin/	0.000103540742669
2300	EmberCoin	https://coinmarketcap.com/currencies/embercoin/	3.19403080262e-08
2301	Birds	https://coinmarketcap.com/currencies/birds/	0.000113319428246
2302	Wink	https://coinmarketcap.com/currencies/wink/	0.000208222948677
2303	SIGMAcoin	https://coinmarketcap.com/currencies/sigmacoin/	0.000890211228691
2304	Moving Cloud ...	https://coinmarketcap.com/currencies/moving-cloud-coin/	0.00344958131257
2305	iQuant	https://coinmarketcap.com/currencies/iquant/	0.0120251728972
2306	Dutch Coin	https://coinmarketcap.com/currencies/dutch-coin/	7.1421853972e-05
2307	Runners	https://coinmarketcap.com/currencies/runners/	9.3452683354e-05
2308	OceanChain	https://coinmarketcap.com/currencies/oceanchain/	0.000413273679581
2309	ValueChain	https://coinmarketcap.com/currencies/valuechain/	0.00338280266902
2310	Animation Vis...	https://coinmarketcap.com/currencies/animation-vision-cash/	0.000211715608078
2311	Superior Coin	https://coinmarketcap.com/currencies/superior-coin/	0.000103793370334
2312	Lendroid Supp...	https://coinmarketcap.com/currencies/lendroid-support-token/	0.000291980605163
2313	SnipCoin	https://coinmarketcap.com/currencies/snipcoin/	2.33591958931e-05
2314	Budbo	https://coinmarketcap.com/currencies/budbo/	0.0033825950267
2315	Cropcoin	https://coinmarketcap.com/currencies/cropcoin/	0.000103605688551
2316	ContractNet	https://coinmarketcap.com/currencies/contractnet/	0.0083354397479
2317	SalPay	https://coinmarketcap.com/currencies/salpay/	0.0205488702445
2318	FToken	https://coinmarketcap.com/currencies/ftoken/	0.125449204587
2319	Haracoin	https://coinmarketcap.com/currencies/haracoin/	0.000306290272395
2320	XTRD	https://coinmarketcap.com/currencies/xtrd/	0.00105521328567
2321	Ultra Salescloud	https://coinmarketcap.com/currencies/ultra-salescoud/	0.000885624032484
2322	BingoCoin	https://coinmarketcap.com/currencies/bingocoin/	0.00125976703693
2323	Ordocoin	https://coinmarketcap.com/currencies/ordocoin/	1.04378346183e-05
2324	PayDay Coin	https://coinmarketcap.com/currencies/payday-coin/	0.000217266171608
2325	CEDEX Coin	https://coinmarketcap.com/currencies/cedex-coin/	0.0136527214408
2326	Pecunio	https://coinmarketcap.com/currencies/pecunio/	0.0494027369054
2327	Obitan Chain	https://coinmarketcap.com/currencies/obitan-chain/	4.06025391129e-05
2328	Hybrid Block	https://coinmarketcap.com/currencies/hybrid-block/	0.000729744964103
2329	Alttex	https://coinmarketcap.com/currencies/alttex/	0.000317164259065
2330	RRCoin	https://coinmarketcap.com/currencies/rrcoin/	0.000128393156918
2331	YUKI	https://coinmarketcap.com/currencies/yuki/	3.45515798895e-06
2332	Centaure	https://coinmarketcap.com/currencies/centaure/	0.000105756400589
2333	ABCC Token	https://coinmarketcap.com/currencies/abcc-token/	0.0422719641968
2334	Crypto Improv...	https://coinmarketcap.com/currencies/crypto-improvement-fund/	0.000106737729202
2335	Coin2Play	https://coinmarketcap.com/currencies/coin2play/	0.000105968744209
2336	Digital Asset...	https://coinmarketcap.com/currencies/digital-asset-exchange-token/	0.000910967850669
2337	Cobrabytes	https://coinmarketcap.com/currencies/cobrabytes/	0.000100731025488
2338	EmaratCoin	https://coinmarketcap.com/currencies/emaratcoin/	0.00092255245776
2339	Bgogo Token	https://coinmarketcap.com/currencies/bgogo-token/	0.00179276859372
2340	TOKOK	https://coinmarketcap.com/currencies/tokok/	0.00440654558202
2341	BiNGO.Fun	https://coinmarketcap.com/currencies/bingo-fun/	0.000319034475139
2342	RoboCalls	https://coinmarketcap.com/currencies/robocalls/	0.000165917568803
2343	Cryptoinvest	https://coinmarketcap.com/currencies/cryptoinvest/	0.000381543573202
2344	HUDDL	https://coinmarketcap.com/currencies/huddl/	0.00419372140679
2345	GoldenFever	https://coinmarketcap.com/currencies/goldenfever/	0.00909606852765
2346	UTEMIS	https://coinmarketcap.com/currencies/utemis/	0.00018380738516
2347	BitStash	https://coinmarketcap.com/currencies/bitstash/	9.27600100296e-06
2348	DEXON	https://coinmarketcap.com/currencies/dexon/	0.0150336368605
2349	Hellenic Node	https://coinmarketcap.com/currencies/hellenic-node/	0.000103355999323
2350	Toqqn	https://coinmarketcap.com/currencies/toqqn/	9.13922141053e-05
2351	Lucky Block N...	https://coinmarketcap.com/currencies/lucky-block-network/	0.0134564134981
2352	UNI COIN	https://coinmarketcap.com/currencies/uni-coin/	1.15905772058
2353	ACChain	https://coinmarketcap.com/currencies/acchain/	0.0129215726726
2354	EscrowCoin	https://coinmarketcap.com/currencies/escrowcoin/	0.000210435916041
2355	ALLCOIN	https://coinmarketcap.com/currencies/allcoin/	0.00156869850932
2356	Delizia	https://coinmarketcap.com/currencies/delizia/	0.000166591743075
\.


--
-- Name: coin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.coin_id_seq', 2356, true);


--
-- Name: coin coin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coin
    ADD CONSTRAINT coin_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

