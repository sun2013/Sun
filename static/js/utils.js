var regEmail = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/
var regPhone = /^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/


/**
 * 自定义校验规则
 */
// $.fn.bootstrapValidator.validators = {
//     phoneOrEmail: {
//         /**
//         * @param {BootstrapValidator} 表单验证实例对象
//         * @param {jQuery} $field jQuery 对象
//         * @param {Object} 表单验证配置项值
//         * @returns {boolean}
//         */
//         validate: function (validator, $field, options) {
//             // 表单输入的值
//             // var value = $field.val();
//             //options为<validatorOptions>对象，直接.获取需要的值
//             // 返回true/false
//             //也可返回{ valid : true/false, message: 'XXXX'}
//             return reg.test($field.val());
//         }
//     },
// };