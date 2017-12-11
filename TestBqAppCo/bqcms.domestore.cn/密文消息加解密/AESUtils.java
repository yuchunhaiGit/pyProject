package com.bingqiong.bq.comm.utils.aes;

import com.bingqiong.bq.comm.exception.BizException;

/**
 * **********************************************************
 * 内容摘要	：<p>
 * <p>
 * 作者	：94841
 * 创建时间	：2016年4月25日 下午1:27:58
 * 当前版本号：v1.0
 * 历史记录	:
 * 日期	: 2016年4月25日 下午1:27:58 	修改人：niuzan
 * 描述	:
 * **********************************************************
 */
public class AESUtils {
    private static String passKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQhIvT60RAT0FJ8tqlV9wN1i8hE37h3IXOxxBwAxkqonFgHw8ucGKT3w8ApGhEgvdRegkHM8/y8MB3l/Q1YOdQMq5DNV5/nHSuYZOTyPE7YlgRj6Xve9KgsRdQT76JIPfCyJd2qCZzsVxsUENZppYPZHAITiOvd8zK9M4cagtkJwIDAQAB";

    public static String encrypt(String content) throws BizException {
        return AESCoder.getEncryptResult(content, passKey);
    }

    public static String decrypt(String content) throws BizException {
        return AESCoder.getDecryptResult(content, passKey);
    }

    public static String getPassKey() {
        return passKey;
    }


    public static void setPassKey(String passKey) {
        AESUtils.passKey = passKey;
    }
}
