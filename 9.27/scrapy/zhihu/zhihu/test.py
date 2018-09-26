import time
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/62.0',
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive'
    'Content-Length''400',
    'content-type':'application/x-www-form-urlencoded',
    'Cookie':'q_c1=294bf23c43dc470b9ba99a3e05278fef|1536117177000|1526395474000; _zap=697155f2-5b86-42d7-9bac-c1ea20d9c973; _xsrf=1oW6sMaaL2P8443J6GF0qrvXGgLrWToC; d_c0="AHAmotL8KQ6PTvjByvuWSqPRZJaH3PbjO6w=|1536115907"; capsion_ticket="2|1:0|10:1536555026|14:capsion_ticket|44:N2MwZTM0YzAyYWI0NDBhYWJjNzU2NTFlMmZhMjUxNjA=|9734e4238915bc665ebb8289b291d295461f183e85ed20980a41535726e44e7e"; r_cap_id="MWUxZjFjYWI0ZDAwNDAzNzkwZDFlYWVhNTI5MWQ4M2M=|1536115917|586dd41527fdce031e72a0428e9e3ca59db502f7"; cap_id="OGVlMjdhOTkxMmRiNGYxNzhkMmU5NmU1MmJlMTY0Yzk=|1536115917|4155eeaa48a09e0e99333a52fa878b813cd34964"; l_cap_id="MWVkOTNhYTJhNGQzNDNmZTlmMTE2ZDFmMGI5ZWQ2MzE=|1536115917|167e0e1ea2903950de5b77fae26f2c8b58a1381a"; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186',
    'Host':'www.zhihu.com',
    'origin':'https://www.zhihu.com',
    'Referer':'https://www.zhihu.com/signup?next=%2F',
    'TE':'Trailers',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'x-ab-param':'top_hweb=0;top_keywordab=0;se_tf=1;top_memberfree=1;top_gif=0;top_gr_topic_reweight=0;web_ask_flow=exp_a;top_billab=0;top_feedre_itemcf=31;top_tr=0;top_feedre_cpt=101;top_feedre=1;top_sjre=0;top_nad=1;top_hqt=0;top_billboard_count=1;se_syn=0;top_yc=0;top_adpar=0;top_manual_tag=1;top_bill=0;top_recall_tb=1;top_new_user_gift=0;tp_ios_topic_write_pin_guide=1;se_daxuechuisou=old;top_card=-1;top_root_ac=-1;top_retagg=0;top_tffrt=0;top_root=0;top_billread=1;top_f_r_nb=1;se_entity=off;top_nszt=0;top_billvideo=0;top_newfollow=0;top_video_fix_position=0;top_recommend_topic_card=0;top_raf=n;se_major_onebox=major;top_an=0;top_sj=2;top_root_web=0;top_uit=0;pin_ef=orig;pin_efs=orig;top_lowup=1;top_root_few_topic=0;top_billpic=0;top_cc_at=-1;top_tmt=0;top_recall=1;ls_play_continuous_order=1;top_test_4_liguangyi=1;top_retag=0;top_free_content=-1;top_recall_tb_long=51;top_30=0;top_follow_reason=0;top_mlt_model=0;top_fqa=0;top_nid=0;top_hca=0;top_vdio_rew=0;tp_sft=a;top_nuc=0;top_feedtopiccard=1;top_recall_tb_short=61;web_logoc=blue;top_ebook=0;top_topic_feedre=21;se_minor_onebox=nd;top_gr_model=0;top_nmt=0;top_login_card=1;top_alt=0;top_multi_model=0;top_billupdate=0;top_universalebook=1;se_gemini_service=content;top_billupdate1=2;top_tag_isolation=0;top_gr_auto_model=0;top_root_mg=1;tp_write_pin_guide=1;top_nucc=0;top_keyword=0;top_ntr=1;se_wiki_box=0;top_video_rew=0;top_user_gift=0;se_dt=0;top_quality=0;top_is_gr=0;top_recall_tb_follow=71;top_tagore=1;top_followtop=0;top_yhgc=0;top_feedre_rtt=41;se_gi=0;top_dtmt=2;top_pfq=0',
    'x-requested-with':'fetch',
    'x-udid':'AHAmotL8KQ6PTvjByvuWSqPRZJaH3PbjO6w=',
    'x-xsrftoken':'1oW6sMaaL2P8443J6GF0qrvXGgLrWToC',
    'x-zse-83':'3_1.1',
}
sss = '分析大V的用户群体'
params = 'Xlrh0D01PXAq4Pe2kx8k0KPx6-fvHXeyXlrh0D01PXAq4xuxjx8k01PwclbfBTuwtx8k0ORk0cus8pf1wlAlMKpmS1NbPoNkjcr2Jd03clbf9hRzmlR1609lMsMbQsbmj_NkKSKkLwr_ahrljsapNKpxHdQtMtQ1kx8k0K5w80raAhQl4xrxMWtlOoQa0pbx4dAxQ5dlTcAbAtNwlgbx7D0l9tu4Nsqxjtf262PxDlRbMs7w12BjPdtyCDRdHXQwXlrh0D01PXAqQgrhncrlSG_kPsbbQkrlgoOk09sz6pBq0Puylx8k0O01J2BqNde1Xlrh00s3OXtrIdA13x8k095k0-NbLkrxgcAl0-owNgu_Albl-crwQWKwRwev8lNwXlrh9-PvOTevDLQw'