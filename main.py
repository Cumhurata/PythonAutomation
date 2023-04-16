from ServisIslemleri import ServiceProcess
from DatabaseBaglantisi import OracleDB

cross_offer_outcome = [
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Accepted"}, {"outcome_id": "31"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Rejected"}, {"outcome_id": "32"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Indecisive"}, {"outcome_id": "34"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "NotOffered"}, {"outcome_id": "37"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "NotReached"}, {"outcome_id": "36"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "NotReached_UH"},
     {"outcome_id": "45"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Ongoing"}, {"outcome_id": "33"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "GotAppointment"},
     {"outcome_id": "48"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "LimitTransferTeklifi_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUBASVNAKIT"}, {"suppress_cdm_ref_id": "Proposition 195"},
     {"suppress_product_group_id": "4"}]]

product_offer_outcome = [
    [{"customer_id": "'1008917620'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Accepted"}, {"outcome_id": "31"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "OfferSelfContention"}, {"suppress_offer_pyname": "KrediKartiLimitArtisi_Branch"},
     {"suppress_channel": "Branch"}, {"suppress_sub_channel": "100101"},
     {"suppress_functionCode": "FIZ"}, {"suppress_cdm_ref_id": "Proposition 37"},
     {"suppress_product_group_id": "4"}],
    [{"customer_id": "'1008914320'"}, {"channel": "Branch"}, {"sub_channel": "100101"}, {"functionCode": "FIZ"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Accepted"}, {"outcome_id": "31"},
     {"suppression": 14}, {"cdm_ref_id": "Proposition 37"}, {"product_group_id": "4"},
     {"pyname": "KrediKartiLimitArtisi_Branch"},
     {"test_case": "OfferSelfContention"}, {"suppress_offer_pyname": "KrediKartiLimitArtisi_Branch"},
     {"suppress_channel": "Branch"}, {"suppress_sub_channel": "100101"},
     {"suppress_functionCode": "FIZ"}, {"suppress_cdm_ref_id": "Proposition 37"},
     {"suppress_product_group_id": "4"}]]

service = ServiceProcess()


def context_data_definition(channel, subchannel, functionCode, orgLevel, userRole):
    if channel == "Branch":
        context_data = "requester==GetOffers;;DynamicPriceTestEnvironment==Default;;channel==" + channel + ";;subchannel==" + subchannel + ";;LogicType==Retention,CrossSell;;customerInContact==false;;fetchAll==true;;functionCode==" + functionCode + ";;FunctionDataList::SMARTLISTPRODUCTCODES==1|LOG_CALL_SOURCE==GO_FIZ;;UserContext::orgLevel==" + orgLevel + "|userRole==" + userRole + "|username==48018"
        return context_data
    if channel == "Mobile":
        context_data = "requester==GetOffers;;DynamicPriceTestEnvironment==Default;;channel==" + channel + ";;subchannel==" + subchannel + ";;LogicType==Retention,CrossSell;;customerInContact==false;;fetchAll==false;;functionCode==" + functionCode + ";;FunctionDataList::OS_NAME==IOS|APP_VERSION==042000|LOG_CALL_SOURCE==GTO"
        return context_data


def cross_offer_ih_check_dif_channel(cust_id, channel, subchannel, functionCode, orgLevel, userRole, outcome,
                                     outcome_id, pyname, suppression_time_temp, suppress_channel, suppress_sub_channel,
                                     suppress_functionCode, suppress_offer_pyname):
    print(f"\n************************CrossOffer IH CHECK FOR {outcome} TODAY STARTS***********************\n")
    # delete ih
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)
    service_cust_id = cust_id.replace("'", "")
    context_data = context_data_definition(suppress_channel, suppress_sub_channel, suppress_functionCode, orgLevel,
                                           userRole)
    print("getOffer Request and Response:")
    service.getOfferResponse(service_cust_id, context_data, suppress_offer_pyname)
    if service.is_offer_presented:
        print("\nCaptureResponse Request and Response: ")
        service.captureResp(outcome, service_cust_id, outcome_id, suppress_sub_channel, suppress_functionCode)
        print("\ngetOffer Request and Response: ")
        context_data = context_data_definition(channel, subchannel, functionCode, orgLevel,
                                               userRole)
        service.getOfferResponse(service_cust_id, context_data, pyname)
        if service.is_offer_presented:
            print("\nTest Case Failed same day offer is presented")
            database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
            database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
        else:
            print(f"\nIn suppression period: {suppression_time_temp} Outcome: {outcome} Pyname : {pyname}\n")
            date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp)
            print("Outcometime is updated :")
            database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
            service.getOfferResponse(service_cust_id, context_data, pyname)
            if service.is_offer_presented:
                print(f"\nTest Case Failed after {suppression_time_temp}")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
            else:
                print(f"\nIn suppression period: {suppression_time_temp + 1} Outcome: {outcome} Pyname : {pyname}\n")
                date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp + 1)
                print("Outcometime is updated :")
                database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
                print("\ngetOffer service request and Response:")
                service.getOfferResponse(service_cust_id, context_data, pyname)
                if service.is_offer_presented:
                    print("\nDatabase Select Records: ")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
                    print(
                        f"\nTest Case Passed for Suppression Day: {suppression_time_temp + 1} and Outcome: {outcome}\n  and Pyname: {pyname}\n")
                else:
                    print(f"\nTest Case Failed after {suppression_time_temp + 1}")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    else:
        print("offer is not presented")
        database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
        database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)


def cross_offer_cdm_ih_check_dif_channel(cust_id, channel, subchannel, functionCode, orgLevel, userRole, outcome,
                                         outcome_id, pyname, suppression_time_temp, suppress_channel,
                                         suppress_sub_channel,
                                         suppress_functionCode, suppress_offer_pyname, suppress_cdm_ref_id,
                                         suppress_product_group_id):
    print(f"\n************************CrossOffer CDM-IH CHECK FOR {outcome} TODAY STARTS***********************\n")
    # delete ih
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)
    suppress_cdm_ref_id = "'" + suppress_cdm_ref_id + "'"
    suppress_channel = "'" + suppress_channel + "'"
    outcome = "'" + outcome + "'"
    service_cust_id = cust_id.replace("'", "")
    cdm_ih_values = service_cust_id + ", sysdate, " + suppress_cdm_ref_id + ", " + outcome + ", " + outcome_id + ", NULL, " + suppress_product_group_id + ", " + suppress_channel + ", NULL, NULL"
    print("\nCDM-IH Record: ")
    database.insert("APPS.CDM_IH",
                    "MUSTERIID, OUTCOMETIME, CDMREFID, OUTCOME, SUBRESPONSECODE, REASONCODE, PRODUCTGROUP, CHANNEL, PRESENTATIONTYPE, OPERATIONTYPE",
                    cdm_ih_values)
    print("Database record for CDM-IH: ")
    database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)

    print("\ngetOffer Request and Response: ")
    context_data = context_data_definition(channel, subchannel, functionCode, orgLevel,
                                           userRole)
    # Servis çağrıldı
    service.getOfferResponse(service_cust_id, context_data, pyname)
    if service.is_offer_presented:
        # eğer teklif gelirse test case failed
        print("\nTest Case Failed today suppression")
        database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
        database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
    else:
        # 14 gün önceye çekildi
        print(f"\nIn suppression period: {suppression_time_temp} Outcome: {outcome}, Pyname : {pyname} \n")
        date_update = "SYSDATE-" + str(suppression_time_temp)
        print(f"Outcometime is updated : {suppression_time_temp}, for Outcome: {outcome}, Pyname : {pyname}")
        database.delete("CDM_IH", "MUSTERIID = " + cust_id)
        cdm_ih_values = service_cust_id + ", " + date_update + ", " + suppress_cdm_ref_id + ", " + outcome + ", " + outcome_id + ", NULL, " + suppress_product_group_id + ", " + suppress_channel + ", NULL, NULL"
        database.insert("APPS.CDM_IH",
                        "MUSTERIID, OUTCOMETIME, CDMREFID, OUTCOME, SUBRESPONSECODE, REASONCODE, PRODUCTGROUP, CHANNEL, PRESENTATIONTYPE, OPERATIONTYPE",
                        cdm_ih_values)
        print("Database record for CDM-IH")
        database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
        # geOffer sonucunda offer gelirse test case fail
        print("\ngetOffer service Request and Response: ")
        service.getOfferResponse(service_cust_id, context_data, pyname)
        if service.is_offer_presented:
            print(f"\nTest Case Failed at suppression period :{suppression_time_temp}")
            database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
            database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
        else:
            # 15 gün önceye çekilde teklif gelirse test case apssed
            print(f"\nIn suppression period: {suppression_time_temp + 1} Outcome: {outcome}, Pyname : {pyname}\n")
            date_update = "SYSDATE-" + str(suppression_time_temp + 1)
            print(f"Outcometime is updated : {suppression_time_temp + 1}")
            database.delete("CDM_IH", "MUSTERIID = " + cust_id)
            cdm_ih_values = service_cust_id + ", " + date_update + ", " + suppress_cdm_ref_id + ", " + outcome + ", " + outcome_id + ", NULL, " + suppress_product_group_id + ", " + suppress_channel + ", NULL, NULL"
            database.insert("APPS.CDM_IH",
                            "MUSTERIID, OUTCOMETIME, CDMREFID, OUTCOME, SUBRESPONSECODE, REASONCODE, PRODUCTGROUP, CHANNEL, PRESENTATIONTYPE, OPERATIONTYPE",
                            cdm_ih_values)
            database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
            print("\n")
            service.getOfferResponse(service_cust_id, context_data, pyname)
            if service.is_offer_presented:
                print(
                    f"\nTest Case passed for suppression duration : {suppression_time_temp + 1} and for Outcome: {outcome}, Pyname : {pyname}\n")
                print("Database Records: ")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
            else:
                print(f"Test Case Failed at suppression period : {suppression_time_temp + 1}\n")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)


def offer_self_contention_ih_check_dif_channel(cust_id, channel, subchannel, functionCode, orgLevel, userRole, outcome,
                                               outcome_id, pyname, suppression_time_temp, suppress_channel,
                                               suppress_sub_channel,
                                               suppress_functionCode, suppress_offer_pyname):
    print(f"\n************************CrossOffer IH CHECK FOR {outcome} TODAY STARTS***********************\n")

    service_cust_id = cust_id.replace("'", "")
    context_data = context_data_definition(suppress_channel, suppress_sub_channel, suppress_functionCode, orgLevel,
                                           userRole)
    print("getOffer Request and Response:")
    service.getOfferResponse(service_cust_id, context_data, suppress_offer_pyname)
    if service.is_offer_presented:
        print("\nCaptureResponse Request and Response: ")
        service.captureResp(outcome, service_cust_id, outcome_id, suppress_sub_channel, suppress_functionCode)
        print("\ngetOffer Request and Response: ")
        context_data = context_data_definition(channel, subchannel, functionCode, orgLevel,
                                               userRole)
        service.getOfferResponse(service_cust_id, context_data, pyname)
        if service.is_offer_presented:
            print("\nTest Case Failed same day offer is presented")
            database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
            database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
        else:
            print(f"\nIn suppression period: {suppression_time_temp} Outcome: {outcome} Pyname : {pyname}\n")
            date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp)
            print("Outcometime is updated :")
            database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
            service.getOfferResponse(service_cust_id, context_data, pyname)
            if service.is_offer_presented:
                print(f"\nTest Case Failed after {suppression_time_temp}")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
            else:
                print(f"\nIn suppression period: {suppression_time_temp + 1} Outcome: {outcome} Pyname : {pyname}\n")
                date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp + 1)
                print("Outcometime is updated :")
                database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
                print("\ngetOffer service request and Response:")
                service.getOfferResponse(service_cust_id, context_data, pyname)
                if service.is_offer_presented:
                    print("\nDatabase Select Records: ")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
                    print(
                        f"\nTest Case Passed for Suppression Day: {suppression_time_temp + 1} and Outcome: {outcome}\n  and Pyname: {pyname}\n")
                else:
                    print(f"\nTest Case Failed after {suppression_time_temp + 1}")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    else:
        print("offer is not presented")
        database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
        database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)


def suppression_check():
    for b_outcome in cross_offer_outcome:
        customer_id = b_outcome[0]['customer_id']
        channel_tmp = b_outcome[1]['channel']
        subchannel_tmp = b_outcome[2]['sub_channel']
        function_code_tmp = b_outcome[3]['functionCode']
        org_level_tmp = b_outcome[4]['orgLevel']
        user_role_tmp = b_outcome[5]['userRole']
        outcome_tmp = b_outcome[6]['outcome']
        outcome_id_tmp = b_outcome[7]['outcome_id']
        suppression_time_temp = b_outcome[8]['suppression']
        cdm_ref_id_tmp = b_outcome[9]['cdm_ref_id']
        product_group_id_tmp = b_outcome[10]['product_group_id']
        pyname_tmp = b_outcome[11]['pyname']
        test_case_tmp = b_outcome[12]['test_case']
        suppress_offer_pyname_tmp = b_outcome[13]['suppress_offer_pyname']
        suppress_channel_tmp = b_outcome[14]['suppress_channel']
        suppress_sub_channel_tmp = b_outcome[15]['suppress_sub_channel']
        suppress_function_code_tmp = b_outcome[16]['suppress_functionCode']
        suppress_cdm_ref_id_tmp = b_outcome[17]['suppress_cdm_ref_id']
        suppress_product_group_id_tmp = b_outcome[18]['suppress_product_group_id']
        if test_case_tmp == "CrossOffer":
            # IH üzerinden de kontrol edilmesi gerekebilir.
            cross_offer_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                             org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp, pyname_tmp,
                                             suppression_time_temp,
                                             suppress_channel_tmp, suppress_sub_channel_tmp,
                                             suppress_function_code_tmp, suppress_offer_pyname_tmp)
            # Farklı kanal olduğu için CDM-IH üzerinden kontrol edilecek
            cross_offer_cdm_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                                 org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp,
                                                 pyname_tmp,
                                                 suppression_time_temp,
                                                 suppress_channel_tmp, suppress_sub_channel_tmp,
                                                 suppress_function_code_tmp, suppress_offer_pyname_tmp,
                                                 suppress_cdm_ref_id_tmp, suppress_product_group_id_tmp)
        elif test_case_tmp == "ProductGroupSuppression":
            # Aynı product groupta olan iki farklı offer buluruz.
            pass

        elif test_case_tmp == "OfferSelfContention":
            # DATABASE CHECK EDİLİR DAHA ÖNCE KAYIT VAR MI KONTROL EDİLİR. MOBİLE/ CALLCENTER/ BRANCH
            # Write-IH yüzünden te record OLSUN dolasıyla function değişecek ih'ler gitmeyecek.
            offer_self_contention_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                                       org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp,
                                                       pyname_tmp,
                                                       suppression_time_temp,
                                                       suppress_channel_tmp, suppress_sub_channel_tmp,
                                                       suppress_function_code_tmp, suppress_offer_pyname_tmp,
                                                       suppress_cdm_ref_id_tmp, suppress_product_group_id_tmp)
            # CDM-IH okay
            cross_offer_cdm_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                                 org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp,
                                                 pyname_tmp,
                                                 suppression_time_temp,
                                                 suppress_channel_tmp, suppress_sub_channel_tmp,
                                                 suppress_function_code_tmp, suppress_offer_pyname_tmp,
                                                 suppress_cdm_ref_id_tmp, suppress_product_group_id_tmp)
            # getoffer request et ve teklifin geldiğini gör
            # Database check edilir.
            # Suppression day kadar geri alınır
            # Database check edilir.
            # getOffer tetiklenir teklifin gelmediği görülür.
            # Suppression day +1
            # Database check edilir.
            # getOffer tetiklenir teklifin geldiği görülür
            pass
        elif test_case_tmp == "ChannelSuppression":
            pass


if __name__ == '__main__':
    database = OracleDB()
    suppression_check()
    database.close_conenction()
