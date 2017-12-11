package com.bingqiong.bq.comm.utils;


import org.springframework.util.Base64Utils;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;
import java.io.UnsupportedEncodingException;
import java.security.SecureRandom;

@SuppressWarnings("unused")
public final class DESUtil {

    private static final String TAG = "DES";
    public static String KEY = "domestore";
//    private static final Logger log = LoggerFactory.getLogger(FileUtils.class);

    private static SecretKeyFactory keyFactory;


    public static String encrypt(String orig) {
        return encrypt(orig, KEY);
    }

    public static String encrypt(String orig, String desKey) {
        String encryptedData = null;
        try {
//            orig = StringUtil.isEmpty(orig) ? orig :
//                    URLEncoder.encode(orig, "UTF-8");
            // DES算法要求有一个可信任的随机数源
            SecureRandom sr = new SecureRandom();
            // 创建一个密匙工厂，然后用它把DESKeySpec转换成一个SecretKey对象
            SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("DES");
            DESKeySpec deskey = new DESKeySpec(desKey.getBytes());
            SecretKey key = keyFactory.generateSecret(deskey);
            // 加密对象

            Cipher cipher = Cipher.getInstance(TAG);
            cipher.init(Cipher.ENCRYPT_MODE, key, sr);
            // 加密，并把字节数组编码成字符串
//            BASE6
            encryptedData = Base64Utils.encodeToString(cipher.doFinal(orig.getBytes("UTF-8")));
            //加密后移除换行符
            encryptedData = removeLineFeedChar(encryptedData);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (Exception e) {
//            log.error("加密错误，错误信息：", e);
//            throw new DESException("加密错误，错误信息：", e);
        }
        return encryptedData;
    }

    public static String decrypt(String orig) {
        return decrypt(orig, KEY);
    }

    public static String decrypt(String orig, String desKey) {
        //解密前移除换行符
        orig = removeLineFeedChar(orig);
        String decryptedData = null;
        try {
            // DES算法要求有一个可信任的随机数源
            SecureRandom sr = new SecureRandom();
            // 创建一个密匙工厂，然后用它把DESKeySpec转换成一个SecretKey对象
            SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("DES");

            DESKeySpec deskey = new DESKeySpec(desKey.getBytes());
            SecretKey key = keyFactory.generateSecret(deskey);
            // 加密对象
            Cipher cipher = Cipher.getInstance(TAG);
            cipher.init(Cipher.DECRYPT_MODE, key, sr);
            // 加密，并把字节数组编码成字符串
            decryptedData = new String(cipher.doFinal(Base64Utils.decodeFromString(orig)), "UTF-8");
        } catch (Exception e) {
//            log.error("解密错误，错误信息：", e);
//            throw new DESException("解密错误", e);
        }
        return decryptedData;
    }

    private static String removeLineFeedChar(String orig) {
        return orig.replaceAll("\n|\r|\t", "");
    }

}
