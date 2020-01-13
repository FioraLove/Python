function encode64(r) {
    var d, _, m, n, t, h = "", e = "", c = "", f = 0;
    do
        d = r.charCodeAt(f++),
        _ = r.charCodeAt(f++),
        e = r.charCodeAt(f++),
        m = d >> 2,
        n = (3 & d) << 4 | _ >> 4,
        t = (15 & _) << 2 | e >> 6,
        c = 63 & e,
        isNaN(_) ? t = c = 64 : isNaN(e) && (c = 64),
        h = h + keyStr.charAt(m) + keyStr.charAt(n) + keyStr.charAt(t) + keyStr.charAt(c),
        d = _ = e = "",
        m = n = t = c = "";
    while (f < r.length);return h
}
function hex_md5(r) {
    return binl2hex(core_md5(str2binl(r), r.length * chrsz))
}
function b64_md5(r) {
    return binl2b64(core_md5(str2binl(r), r.length * chrsz))
}
function str_md5(r) {
    return binl2str(core_md5(str2binl(r), r.length * chrsz))
}
function hex_hmac_md5(r, d) {
    return binl2hex(core_hmac_md5(r, d))
}
function b64_hmac_md5(r, d) {
    return binl2b64(core_hmac_md5(r, d))
}
function str_hmac_md5(r, d) {
    return binl2str(core_hmac_md5(r, d))
}
function md5_vm_test() {
    return "900150983cd24fb0d6963f7d28e17f72" == hex_md5("abc")
}
function core_md5(r, d) {
    r[d >> 5] |= 128 << d % 32,
    r[(d + 64 >>> 9 << 4) + 14] = d;
    for (var _ = 1732584193, m = -271733879, n = -1732584194, t = 271733878, h = 0; h < r.length; h += 16) {
        var e = _
          , c = m
          , f = n
          , i = t;
        _ = md5_ff(_, m, n, t, r[h + 0], 7, -680876936),
        t = md5_ff(t, _, m, n, r[h + 1], 12, -389564586),
        n = md5_ff(n, t, _, m, r[h + 2], 17, 606105819),
        m = md5_ff(m, n, t, _, r[h + 3], 22, -1044525330),
        _ = md5_ff(_, m, n, t, r[h + 4], 7, -176418897),
        t = md5_ff(t, _, m, n, r[h + 5], 12, 1200080426),
        n = md5_ff(n, t, _, m, r[h + 6], 17, -1473231341),
        m = md5_ff(m, n, t, _, r[h + 7], 22, -45705983),
        _ = md5_ff(_, m, n, t, r[h + 8], 7, 1770035416),
        t = md5_ff(t, _, m, n, r[h + 9], 12, -1958414417),
        n = md5_ff(n, t, _, m, r[h + 10], 17, -42063),
        m = md5_ff(m, n, t, _, r[h + 11], 22, -1990404162),
        _ = md5_ff(_, m, n, t, r[h + 12], 7, 1804603682),
        t = md5_ff(t, _, m, n, r[h + 13], 12, -40341101),
        n = md5_ff(n, t, _, m, r[h + 14], 17, -1502002290),
        m = md5_ff(m, n, t, _, r[h + 15], 22, 1236535329),
        _ = md5_gg(_, m, n, t, r[h + 1], 5, -165796510),
        t = md5_gg(t, _, m, n, r[h + 6], 9, -1069501632),
        n = md5_gg(n, t, _, m, r[h + 11], 14, 643717713),
        m = md5_gg(m, n, t, _, r[h + 0], 20, -373897302),
        _ = md5_gg(_, m, n, t, r[h + 5], 5, -701558691),
        t = md5_gg(t, _, m, n, r[h + 10], 9, 38016083),
        n = md5_gg(n, t, _, m, r[h + 15], 14, -660478335),
        m = md5_gg(m, n, t, _, r[h + 4], 20, -405537848),
        _ = md5_gg(_, m, n, t, r[h + 9], 5, 568446438),
        t = md5_gg(t, _, m, n, r[h + 14], 9, -1019803690),
        n = md5_gg(n, t, _, m, r[h + 3], 14, -187363961),
        m = md5_gg(m, n, t, _, r[h + 8], 20, 1163531501),
        _ = md5_gg(_, m, n, t, r[h + 13], 5, -1444681467),
        t = md5_gg(t, _, m, n, r[h + 2], 9, -51403784),
        n = md5_gg(n, t, _, m, r[h + 7], 14, 1735328473),
        m = md5_gg(m, n, t, _, r[h + 12], 20, -1926607734),
        _ = md5_hh(_, m, n, t, r[h + 5], 4, -378558),
        t = md5_hh(t, _, m, n, r[h + 8], 11, -2022574463),
        n = md5_hh(n, t, _, m, r[h + 11], 16, 1839030562),
        m = md5_hh(m, n, t, _, r[h + 14], 23, -35309556),
        _ = md5_hh(_, m, n, t, r[h + 1], 4, -1530992060),
        t = md5_hh(t, _, m, n, r[h + 4], 11, 1272893353),
        n = md5_hh(n, t, _, m, r[h + 7], 16, -155497632),
        m = md5_hh(m, n, t, _, r[h + 10], 23, -1094730640),
        _ = md5_hh(_, m, n, t, r[h + 13], 4, 681279174),
        t = md5_hh(t, _, m, n, r[h + 0], 11, -358537222),
        n = md5_hh(n, t, _, m, r[h + 3], 16, -722521979),
        m = md5_hh(m, n, t, _, r[h + 6], 23, 76029189),
        _ = md5_hh(_, m, n, t, r[h + 9], 4, -640364487),
        t = md5_hh(t, _, m, n, r[h + 12], 11, -421815835),
        n = md5_hh(n, t, _, m, r[h + 15], 16, 530742520),
        m = md5_hh(m, n, t, _, r[h + 2], 23, -995338651),
        _ = md5_ii(_, m, n, t, r[h + 0], 6, -198630844),
        t = md5_ii(t, _, m, n, r[h + 7], 10, 1126891415),
        n = md5_ii(n, t, _, m, r[h + 14], 15, -1416354905),
        m = md5_ii(m, n, t, _, r[h + 5], 21, -57434055),
        _ = md5_ii(_, m, n, t, r[h + 12], 6, 1700485571),
        t = md5_ii(t, _, m, n, r[h + 3], 10, -1894986606),
        n = md5_ii(n, t, _, m, r[h + 10], 15, -1051523),
        m = md5_ii(m, n, t, _, r[h + 1], 21, -2054922799),
        _ = md5_ii(_, m, n, t, r[h + 8], 6, 1873313359),
        t = md5_ii(t, _, m, n, r[h + 15], 10, -30611744),
        n = md5_ii(n, t, _, m, r[h + 6], 15, -1560198380),
        m = md5_ii(m, n, t, _, r[h + 13], 21, 1309151649),
        _ = md5_ii(_, m, n, t, r[h + 4], 6, -145523070),
        t = md5_ii(t, _, m, n, r[h + 11], 10, -1120210379),
        n = md5_ii(n, t, _, m, r[h + 2], 15, 718787259),
        m = md5_ii(m, n, t, _, r[h + 9], 21, -343485551),
        _ = safe_add(_, e),
        m = safe_add(m, c),
        n = safe_add(n, f),
        t = safe_add(t, i)
    }
    return Array(_, m, n, t)
}
function md5_cmn(r, d, _, m, n, t) {
    return safe_add(bit_rol(safe_add(safe_add(d, r), safe_add(m, t)), n), _)
}
function md5_ff(r, d, _, m, n, t, h) {
    return md5_cmn(d & _ | ~d & m, r, d, n, t, h)
}
function md5_gg(r, d, _, m, n, t, h) {
    return md5_cmn(d & m | _ & ~m, r, d, n, t, h)
}
function md5_hh(r, d, _, m, n, t, h) {
    return md5_cmn(d ^ _ ^ m, r, d, n, t, h)
}
function md5_ii(r, d, _, m, n, t, h) {
    return md5_cmn(_ ^ (d | ~m), r, d, n, t, h)
}
function core_hmac_md5(r, d) {
    var _ = str2binl(r);
    _.length > 16 && (_ = core_md5(_, r.length * chrsz));
    for (var m = Array(16), n = Array(16), t = 0; 16 > t; t++)
        m[t] = 909522486 ^ _[t],
        n[t] = 1549556828 ^ _[t];
    var h = core_md5(m.concat(str2binl(d)), 512 + d.length * chrsz);
    return core_md5(n.concat(h), 640)
}
function safe_add(r, d) {
    var _ = (65535 & r) + (65535 & d)
      , m = (r >> 16) + (d >> 16) + (_ >> 16);
    return m << 16 | 65535 & _
}
function bit_rol(r, d) {
    return r << d | r >>> 32 - d
}
function str2binl(r) {
    for (var d = Array(), _ = (1 << chrsz) - 1, m = 0; m < r.length * chrsz; m += chrsz)
        d[m >> 5] |= (r.charCodeAt(m / chrsz) & _) << m % 32;
    return d
}
function binl2str(r) {
    for (var d = "", _ = (1 << chrsz) - 1, m = 0; m < 32 * r.length; m += chrsz)
        d += String.fromCharCode(r[m >> 5] >>> m % 32 & _);
    return d
}
function binl2hex(r) {
    for (var d = hexcase ? "0123456789ABCDEF" : "0123456789abcdef", _ = "", m = 0; m < 4 * r.length; m++)
        _ += d.charAt(15 & r[m >> 2] >> 8 * (m % 4) + 4) + d.charAt(15 & r[m >> 2] >> 8 * (m % 4));
    return _
}
function binl2b64(r) {
    for (var d = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", _ = "", m = 0; m < 4 * r.length; m += 3)
        for (var n = (255 & r[m >> 2] >> 8 * (m % 4)) << 16 | (255 & r[m + 1 >> 2] >> 8 * ((m + 1) % 4)) << 8 | 255 & r[m + 2 >> 2] >> 8 * ((m + 2) % 4), t = 0; 4 > t; t++)
            _ += 8 * m + 6 * t > 32 * r.length ? b64pad : d.charAt(63 & n >> 6 * (3 - t));
    return _
}
var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
  , hexcase = 0
  , b64pad = ""
  , chrsz = 8;
  
// 调用加密函数
function getPwd(password){
	return encode64(password);
}
