package com.bingqiong.bq.comm.utils.aes;

import com.bingqiong.bq.comm.constants.ErrorCode;
import com.bingqiong.bq.comm.exception.BizException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;

public class AESCoder {

    private static final Logger log = LoggerFactory.getLogger(AESCoder.class);

    private static final String KEY_ALGORITHM = "AES";

    /**
     * 函数名称 : decrypt
     * 功能描述 :
     * 参数及返回值说明：
     *
     * @param content
     * @param salt
     * @return 修改记录：
     * 日期 ：2016年4月25日 下午12:24:40	修改人：  niuzan
     * 描述	：
     */
    public static byte[] decrypt(byte[] content, String salt) throws BizException {
        try {
            KeyGenerator kgen = KeyGenerator.getInstance(KEY_ALGORITHM);
            SecureRandom secureRandom = SecureRandom.getInstance("SHA1PRNG");
            secureRandom.setSeed(salt.getBytes());
            kgen.init(128, secureRandom);
            SecretKey secretKey = kgen.generateKey();
            byte[] enCodeFormat = secretKey.getEncoded();
            SecretKeySpec key = new SecretKeySpec(enCodeFormat, KEY_ALGORITHM);
            Cipher cipher = Cipher.getInstance(KEY_ALGORITHM);// 创建密码器
            cipher.init(Cipher.DECRYPT_MODE, key);// 初始化
            byte[] result = cipher.doFinal(content);
            return result; // 加密
        } catch (Exception e) {
            log.info("消息解密失败！", e);
            throw new BizException(ErrorCode.SYSTEM_EXCEPTION);
        }
    }

    /**
     * 函数名称 : encrypt
     * 功能描述 :
     * 参数及返回值说明：
     *
     * @param content
     * @param salt
     * @param isCheck TODO
     * @return 修改记录：
     * 日期 ：2016年4月25日 下午12:24:49	修改人：  niuzan
     * 描述	：
     */
    public static byte[] encrypt(String content, String salt, boolean isCheck) throws BizException {
        try {
            KeyGenerator kgen = KeyGenerator.getInstance(KEY_ALGORITHM);
            SecureRandom secureRandom = SecureRandom.getInstance("SHA1PRNG");
            secureRandom.setSeed(salt.getBytes());
            kgen.init(128, secureRandom);
            SecretKey secretKey = kgen.generateKey();
            byte[] enCodeFormat = secretKey.getEncoded();
            SecretKeySpec key = new SecretKeySpec(enCodeFormat, KEY_ALGORITHM);
            Cipher cipher = Cipher.getInstance(KEY_ALGORITHM);// 创建密码器
            byte[] byteContent = content.getBytes("utf-8");
            cipher.init(Cipher.ENCRYPT_MODE, key);// 初始化
            byte[] result = cipher.doFinal(byteContent);
            return result; // 加密
        } catch (Exception e) {
            if (!isCheck) {
                log.info("消息加密失败！", e);
                throw new BizException(ErrorCode.SYSTEM_EXCEPTION);
            }
            //当是检查是否是aes加密的场景下，直接抛出异常，不打印日志
            throw new RuntimeException();
        }
    }

    /**
     * 函数名称 : parseByte2HexStr
     * 功能描述 :
     * 参数及返回值说明：
     *
     * @param buf
     * @return 修改记录：
     * 日期 ：2016年4月25日 下午12:25:04	修改人：  niuzan
     * 描述	：
     */
    public static String parseByte2HexStr(byte buf[]) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < buf.length; i++) {
            String hex = Integer.toHexString(buf[i] & 0xFF);
            if (hex.length() == 1) {
                hex = '0' + hex;
            }
            sb.append(hex.toUpperCase());
        }
        return sb.toString();
    }

    /**
     * 函数名称 : parseHexStr2Byte
     * 功能描述 :
     * 参数及返回值说明：
     *
     * @param hexStr
     * @return 修改记录：
     * 日期 ：2016年4月25日 下午12:19:45	修改人：  niuzan
     * 描述	：
     */
    public static byte[] parseHexStr2Byte(String hexStr) {
        try {
            if (hexStr.length() < 1)
                return null;
            byte[] result = new byte[hexStr.length() / 2];
            for (int i = 0; i < hexStr.length() / 2; i++) {
                int high = Integer.parseInt(hexStr.substring(i * 2, i * 2 + 1), 16);
                int low = Integer.parseInt(hexStr.substring(i * 2 + 1, i * 2 + 2), 16);
                result[i] = (byte) (high * 16 + low);
            }
            return result;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * 函数名称 : getEncryptResult
     * 功能描述 :
     * 参数及返回值说明：
     *
     * @param content
     * @param passKey
     * @return 修改记录：
     * 日期 ：2016年4月25日 下午12:24:19	修改人：  niuzan
     * 描述	：
     */
    public static String getEncryptResult(String content, String passKey) throws BizException {
        return parseByte2HexStr(encrypt(content, passKey, false));
    }

    /**
     * 函数名称 : getDecryptResult
     * 功能描述 :
     * 参数及返回值说明：
     *
     * @param content
     * @param passKey
     * @return 修改记录：
     * 日期 ：2016年4月25日 下午12:24:26	修改人：  niuzan
     * 描述	：
     */
    public static String getDecryptResult(String content, String passKey) throws BizException {
        String str = new String(decrypt(parseHexStr2Byte(content), passKey));
        log.info("转为字符串：{}", str);
        return str;
    }


//	public static void main(String[] args) throws Exception
//	{
//		String oripwd = "123456";
//		String content = "RDAwMDEyODQ|YnFfMDAwMDAwMDYw|1493967092559|8f99e0b3ca49c563ff40f234b4fe7bd4";  
//		String salt = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQhIvT60RAT0FJ8tqlV9wN1i8hE37h3IXOxxBwAxkqonFgHw8ucGKT3w8ApGhEgvdRegkHM8/y8MB3l/Q1YOdQMq5DNV5/nHSuYZOTyPE7YlgRj6Xve9KgsRdQT76JIPfCyJd2qCZzsVxsUENZppYPZHAITiOvd8zK9M4cagtkJwIDAQAB";  
//		//加密   
//		System.out.println("加密前：" + oripwd);
//		byte[] encryptResult = encrypt(oripwd, salt, true);
//		String encryptResultStr = parseByte2HexStr(encryptResult);
//		System.out.println("加密后：" + encryptResultStr);
//		//解密   
////		byte[] decryptFrom = parseHexStr2Byte(content);  
////		byte[] decryptResult = decrypt(decryptFrom,salt);  
////		System.out.println("解密后：" + new String(decryptResult));  
//		
//	}

}
