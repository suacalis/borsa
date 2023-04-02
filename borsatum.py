import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf # https://pypi.org/project/yfinance/

###########
# sidebar #
###########
option = st.sidebar.selectbox('Select one symbol', ('ADEL.IS', 'ADESE.IS', 'AEFES.IS', 'df.IS', 'AGESA.IS', 'AGHOL.IS', 'AGYO.IS', 'AHGAZ.IS', 'AKBNK.IS', 'AKCNS.IS', 'AKENR.IS', 'AKFGY.IS', 'AKFYE.IS', 'AKGRT.IS', 'AKMGY.IS', 'AKSA.IS', 'AKSEN.IS', 'AKSGY.IS', 'AKSUE.IS', 'AKYHO.IS', 'ALARK.IS', 'ALBRK.IS', 'ALCAR.IS', 'ALCTL.IS', 'ALFAS.IS', 'ALGYO.IS', 'ALKA.IS', 'ALKIM.IS', 'ALMAD.IS', 'ALTINS1.IS', 'ANELE.IS', 'ANGEN.IS', 'ANHYT.IS', 'ANSGR.IS', 'ARASE.IS', 'ARCLK.IS', 'ARDYZ.IS', 'ARENA.IS', 'ARMDA.IS', 'ARSAN.IS', 'ARZUM.IS', 'ASELS.IS', 'ASTOR.IS', 'ASUZU.IS', 'ATAGY.IS', 'ATATP:IS', 'ATEKS.IS', 'ATLAS.IS', 'ATSYH.IS', 'AVGYO.IS', 'AVHOL.IS', 'AVOD.IS', 'AVTUR.IS', 'AYCES.IS', 'AYDEM.IS', 'AYEN.IS', 'AYES.IS', 'AYGAZ.IS', 'AZTEK.IS', 'BAGFS.IS', 'BAKAB.IS', 'BALAT.IS', 'BANVT.IS', 'BARMA.IS', 'BASCM.IS', 'BASGZ.IS', 'BAYRK.IS', 'BERA.IS', 'BEYAZ.IS', 'BFREN.IS', 'BIMAS.IS', 'BIOEN.IS', 'BIZIM.IS', 'BJKAS.IS', 'BLCYT.IS', 'BMSCH.IS', 'BMSTL.IS', 'BNTAS.IS', 'BOBET.IS', 'BOSSA.IS', 'BRISA.IS', 'BRKO.IS', 'BRKSN.IS', 'BRKVY.IS', 'BRLSM.IS', 'BRMEN.IS', 'BRSAN.IS', 'BRYAT.IS', 'BSOKE.IS', 'BTCIM.IS', 'BUCIM.IS', 'BURCE.IS', 'BURVA.IS', 'BVSAN.IS', 'CANTE.IS', 'CASA.IS', 'CCOLA.IS', 'CELHA.IS', 'CEMAS.IS', 'CEMTS.IS', 'CEOEM.IS', 'CIMSA.IS', 'CLEBI.IS', 'CMBTN.IS', 'CMENT.IS', 'CONSE.IS', 'COSMO.IS', 'CRDFA.IS', 'CRFSA.IS', 'CUSAN.IS', 'DAGHL.IS', 'DAGI.IS', 'DAPGM.IS', 'DARDL.IS', 'DENGE.IS', 'DERHL.IS', 'DERIM.IS', 'DESA.IS', 'DESPC.IS', 'DEVA.IS', 'DGATE.IS', 'DGGYO.IS', 'DGNMO.IS', 'DIRIT.IS', 'DITAS.IS', 'DMSAS.IS', 'DNISI.IS', 'DOAS.IS', 'DOBUR.IS', 'DOCO.IS', 'DOGUB.IS', 'DOHOL.IS', 'DOKTA.IS', 'DURDO.IS', 'DYOBY.IS', 'DZGYO.IS', 'ECILC.IS', 'ECZYT.IS', 'EDATA.IS', 'EDIP.IS', 'EGEEN.IS', 'EGEPO.IS', 'EGGUB.IS', 'EGPRO.IS', 'EGSER.IS', 'EKGYO.IS', 'EKIZ.IS', 'EKSUN.IS', 'ELITE.IS', 'EMKEL.IS', 'EMNIS.IS', 'ENJSA.IS', 'ENKAI.IS', 'ENSRI.IS', 'EPLAS.IS', 'ERBOS.IS', 'ERCB.IS', 'EREGL.IS', 'ERSU.IS', 'ESCAR.IS', 'ESCOM.IS', 'ESEN.IS', 'ETILR.IS', 'ETYAT.IS', 'EUHOL.IS', 'EUKYO.IS', 'EUREN.IS', 'EUYO.IS', 'EYGYO.IS', 'FADE.IS', 'FENER.IS', 'FLAP.IS', 'FMIZP.IS', 'FONET.IS', 'FORMT.IS', 'FRIGO.IS', 'FROTO.IS', 'GARAN.IS', 'GARFA.IS', 'GEDIK.IS', 'GEDZA.IS', 'GENIL.IS', 'GENTS.IS', 'GEREL.IS', 'GESAN.IS', 'GLBMD.IS', 'GLCVY.IS', 'GLRYH.IS', 'GLYHO.IS', 'GMTAS.IS', 'GOKNR.IS', 'GOLTS.IS', 'GOODY.IS', 'GOZDE.IS', 'GRNYO.IS', 'GRSEL.IS', 'GSDDE.IS', 'GSDHO.IS', 'GSRAY.IS', 'GUBRF.IS', 'GWIND.IS', 'GZNMI.IS', 'HALKB.IS', 'HATEK.IS', 'HDFGS.IS', 'HEDEF.IS', 'HEKTS.IS', 'HKTM.IS', 'HLGYO.IS', 'HTTBT.IS', 'HUBVC.IS', 'HUNER.IS', 'HURGZ.IS', 'ICBCT.IS', 'IDEAS.IS', 'IDGYO.IS', 'IEYHO.IS', 'IHAAS.IS', 'IHEVA.IS', 'IHGZT.IS', 'IHLAS.IS', 'IHLGM.IS', 'IHYAY.IS', 'IMASM.IS', 'INDES.IS', 'INFO.IS', 'INTEM.IS', 'INVEO.IS', 'INVES.IS', 'IPEKE.IS', 'ISATR.IS', 'ISBIR.IS', 'ISBTR.IS', 'ISCTR.IS', 'ISDMR.IS', 'ISFIN.IS', 'ISGSY.IS', 'ISGYO.IS', 'ISKPL.IS', 'ISKUR.IS', 'ISMEN.IS', 'ISSEN.IS', 'ISYAT.IS', 'ITTFH.IS', 'IZFAS.IS', 'IZINV.IS', 'IZMDC.IS', 'JANTS.IS', 'KAPLM.IS', 'KAREL.IS', 'KARSN.IS', 'KARTN.IS', 'KARYE.IS', 'KATMR.IS', 'KCAER.IS', 'KCHOL.IS', 'KENT.IS', 'KERVN.IS', 'KERVT.IS', 'KFEIN.IS', 'KGYO.IS', 'KIMMR.IS', 'KLGYO.IS', 'KLKIM.IS', 'KLMSN.IS', 'KLNMA.IS', 'KLRHO.IS', 'KLSYN.IS', 'KMPUR.IS', 'KNFRT.IS', 'KONKA.IS', 'KONTR.IS', 'KONYA.IS', 'KORDS.IS', 'KOZAA.IS', 'KOZAL.IS', 'KRDMA.IS', 'KRDMB.IS', 'KRDMD.IS', 'KRGYO.IS', 'KRONT.IS', 'KRPLS.IS', 'KRSTL.IS', 'KRTEK.IS', 'KRVGD.IS', 'KSTUR.IS', 'KTSKR.IS', 'KUTPO.IS', 'KUVVA.IS', 'KUYAS.IS', 'KZBGY.IS', 'LIDER.IS', 'LIDFA.IS', 'LINK.IS', 'LKMNH.IS', 'LOGO.IS', 'LUKSK.IS', 'MAALT.IS', 'MACKO.IS', 'MAGEN.IS', 'MAKIM.IS', 'MAKTK.IS', 'MANAS.IS', 'MARKA.IS', 'MARTI.IS', 'MAVI.IS', 'MEDTR.IS', 'MEGAP.IS', 'MEPET.IS', 'MERCN.IS', 'MERIT.IS', 'MERKO.IS', 'METRO.IS', 'METUR.IS', 'MGROS.IS', 'MIATK.IS', 'MIPAZ.IS', 'MMCAS.IS', 'MNDRS.IS', 'MNDTR.IS', 'MOBTL.IS', 'MPARK.IS', 'MRGYO.IS', 'MRSHL.IS', 'MSGYO.IS', 'MTRKS.IS', 'MTRYO.IS', 'MZHLD.IS', 'NATEN.IS', 'NETAS.IS', 'NIBAS.IS', 'NTGAZ.IS', 'NTHOL.IS', 'NUGYO.IS', 'NUHCM.IS', 'OBASE.IS', 'ODAS.IS', 'ONCSM.IS', 'ORCAY.IS', 'ORGE.IS', 'ORMA.IS', 'OSMEN.IS', 'OSTIM.IS', 'OTKAR.IS', 'OTTO.IS', 'OYAKC.IS', 'OYAYO.IS', 'OYLUM.IS', 'OYYAT.IS', 'OZGYO.IS', 'OZKGY.IS', 'OZRDN.IS', 'OZSUB.IS', 'PAGYO.IS', 'PAMEL.IS', 'PAPIL.IS', 'PARSN.IS', 'PCILT.IS', 'PEGYO.IS', 'PEKGY.IS', 'PENGD.IS', 'PENTA.IS', 'PETKM.IS', 'PETUN.IS', 'PGSUS.IS', 'PINSU.IS', 'PKART.IS', 'PKENT.IS', 'PLTUR.IS', 'PNLSN.IS', 'PNSUT.IS', 'POLHO.IS', 'POLTK.IS', 'PRDGS.IS', 'PRKAB.IS', 'PRKME.IS', 'PRZMA.IS', 'PSDTC.IS', 'PSGYO.IS', 'QNBFB.IS', 'QNBFL.IS', 'QUAGR.IS', 'RALYH.IS', 'RAYSG.IS', 'RHEAG.IS', 'RNPOL.IS', 'RODRG.IS', 'ROYAL.IS', 'RTALB.IS', 'RUBNS.IS', 'RYGYO.IS', 'RYSAS.IS', 'SAFKR.IS', 'SAHOL.IS', 'SAMAT.IS', 'SANEL.IS', 'SANFM.IS', 'SANKO.IS', 'SARKY.IS', 'SASA.IS', 'SAYAS.IS', 'SDTTR.IS', 'SEGYO.IS', 'SEKFK.IS', 'SEKUR.IS', 'SELEC.IS', 'SELGD.IS', 'SELVA.IS', 'SEYKM.IS', 'SILVR.IS', 'SISE.IS', 'SKBNK.IS', 'SKTAS.IS', 'SMART.IS', 'SMRTG.IS', 'SNGYO.IS', 'SNICA.IS', 'SNKRN.IS', 'SNPAM.IS', 'SODSN.IS', 'SOKE.IS', 'SOKM.IS', 'SONME.IS', 'SRVGY.IS', 'SUMAS.IS', 'SUNTK.IS', 'SUWEN.IS', 'TATGD.IS', 'TAVHL.IS', 'TBORG.IS', 'TCELL.IS', 'TDGYO.IS', 'TEKTU.IS', 'TERA.IS', 'TETMT.IS', 'TEZOL.IS', 'TGSAS.IS', 'THYAO.IS', 'TKFEN.IS', 'TKNSA.IS', 'TLMAN.IS', 'TMPOL.IS', 'TMSN.IS', 'TNZTP.IS', 'TOASO.IS', 'TRCAS.IS', 'TRGYO.IS', 'TRILC.IS', 'TSGYO.IS', 'TSKB.IS', 'TSPOR.IS', 'TTKOM.IS', 'TTRAK.IS', 'TUCLK.IS', 'TUKAS.IS', 'TUPRS.IS', 'TUREX.IS', 'TURGG.IS', 'TURSG.IS', 'UFUK.IS', 'ULAS.IS', 'ULKER.IS', 'ULUFA.IS', 'ULUSE.IS', 'ULUUN.IS', 'UMPAS.IS', 'UNLU.IS', 'USAK.IS', 'UZERB.IS', 'VAKBN.IS', 'VAKFN.IS', 'VAKKO.IS', 'VANGD.IS', 'VBTYZ.IS', 'VERTU.IS', 'VERUS.IS', 'VESBE.IS', 'VESTL.IS', 'VKFYO.IS', 'VKGYO.IS', 'VKING.IS', 'YAPRK.IS', 'YATAS.IS', 'YAYLA.IS', 'YBTAS.IS', 'YEOTK.IS', 'YESIL.IS', 'YGGYO.IS', 'YGYO.IS', 'YKBNK.IS', 'YKSLN.IS', 'YONGA.IS', 'YUNSA.IS', 'YYAPI.IS', 'YYLGD.IS', 'ZEDUR.IS', 'ZOREN.IS', 'ZRGYO.IS'))
import datetime

today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')


df = yf.download(option,start= start_date,end= end_date, progress=False)

import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Calculation of momentum
df['momentum'] = df['Close'].pct_change()

# Creating subplots to show momentum and buying/selling markers
figure = make_subplots(rows=2, cols=1)
figure.add_trace(go.Scatter(x=df.index, 
                         y=df['Close'], 
                         name='Close Price'))
figure.add_trace(go.Scatter(x=df.index, 
                         y=df['momentum'], 
                         name='Momentum', 
                         yaxis='y2'))

# Adding the buy and sell signals
figure.add_trace(go.Scatter(x=df.loc[df['momentum'] > 0].index, 
                         y=df.loc[df['momentum'] > 0]['Close'], 
                         mode='markers', name='Buy', 
                         marker=dict(color='green', symbol='triangle-up')))

figure.add_trace(go.Scatter(x=df.loc[df['momentum'] < 0].index, 
                         y=df.loc[df['momentum'] < 0]['Close'], 
                         mode='markers', name='Sell', 
                         marker=dict(color='red', symbol='triangle-down')))

figure.update_layout(title='Kağıt',
                  xaxis_title='Date',
                  yaxis_title='Price')
figure.update_yaxes(title="Momentum", secondary_y=True)

# Show the figure using Streamlit
st.plotly_chart(figure)
