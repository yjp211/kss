(function($) {
	/*
	 Validation Singleton
	 */
	var Validation = function() {

		var rules = {
			date : {
				check : function(value) {
					if(value){
						var re = /^(\d{4})-(\d{2})-(\d{2})$/g;
						if(re.test(value)){
							if((RegExp.$1 > 1900) && (RegExp.$1 < 9999) && (RegExp.$2 > 0) && (RegExp.$2 < 13) && (RegExp.$3 > 0) && (RegExp.$3 < 32)){
								return true;
							}
						}
						return false
					}
					return true;
				},
				msg : "日期格式不对"
			}, 
			newPasswdCommit : {
				check : function(value) {
					//alert(value);
					if(document.getElementById("newPasswdCommit").value == document.getElementById("newPasswd").value){
						return true;
					}
					return false;
				},
				msg : "两次输入的密码不一致"
			}, 
			start : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^()([0-9]+(\.[0-9]+)?)((([k|K|m|M|g|G|t|T])[b|B]?)|%)$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "示例:20GB/20％"
			}, 
			end : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^([+]?)([0-9]+(\.[0-9]+)?)((([k|K|m|M|g|G|t|T])[b|B]?)|%)$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "示例:20GB/+20％"
			},
			yesno : {
				check : function(value) {
					if(value){
						var re = /^([y|Y][e|E][s|S])$|([n|N][o|O])$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "请输入yes或no"
			},
			normal : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^[0-9a-zA-Z\-_\u4e00-\u9fa5]+$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "包含非法字符"
			},
			name : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^[a-zA-Z]+[0-9a-zA-Z]*$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "字母开头，只包含字母数字"
			},
			path : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^[\/0-9a-zA-Z_\u4e00-\u9fa5\-\.]+$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "非法路径"
			},
			pathName : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^[0-9a-zA-Z_\u4e00-\u9fa5\-\.]+$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "非法文件名"
			},
			fileMod : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^[0-7]{3,4}$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "非法文件权限"
			},
			num : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^[-+]?[0-9]+$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "请输入整数"
			},
			percentNum : {
				check : function(value) {
					if(value){
						var re = /^(\d+)$/;
						if(re.test(value)){
							if(RegExp.$1<=100 && RegExp.$1>=0){
									return true
							}
						}
						return false;
						
					}
					return true;
				},
				msg : "请输入0~100有效数字"
			},
			inter : {
				check : function(value) {
					//alert(value);
					if(value){
						var re = /^[0-9a-zA-Z_]+$/;
						if(re.test(value)){
							return true;
						}
						return false;
					}
					return true;
				},
				msg : "非法接口名称"
			},
			gateway : {
				check : function(value) {
					if(value){
						var re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
						if(re.test(value)){
							if(RegExp.$1<256 && RegExp.$2<256
								&& RegExp.$3<256 && RegExp.$4<256){
									return true
							}
						}
						return false;
						
					}
						
					return true;
				},
				msg : "非法网关"
			},
			mask : {
				check : function(value) {
					if(value){
						var re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
						if(re.test(value)){
							if(RegExp.$1<256 && RegExp.$2<256
								&& RegExp.$3<256 && RegExp.$4<256){
									return true
							}
						}
						return false;
						
					}
						
					return true;
				},
				msg : "非法掩码"
			},
			ip : {
				check : function(value) {
					if(value){
						var re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
						if(re.test(value)){
							if(RegExp.$1<256 && RegExp.$2<256
								&& RegExp.$3<256 && RegExp.$4<256){
									return true
							}
						}
						return false;
						
					}
						
					return true;
				},
				msg : "非法地址"
			},
			iplist : {
				check : function(value) {
					if(value){
						var iplist = value.split(' ');
						var re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
						for(var i=0; i <= iplist.length; i++){
							var ip = iplist[i];
							if(ip){
								if(re.test(ip)){
									if(RegExp.$1<256 && RegExp.$2<256
										&& RegExp.$3<256 && RegExp.$4<256){
											continue;
									}else{
										return false;
									}
								}else{
									return false;
								}
							}
							
						}
						return true;
						
					}
						
					return true;
				},
				msg : "非法地址列表"
			},
			ipAndMask : {
				check : function(value) {
					if(value){
						var re1 = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
						var re2 = /^(\d+)\.(\d+)\.(\d+)\.(\d+)\/\d+$/;
						if(re1.test(value)){
							if(RegExp.$1<256 && RegExp.$2<256
								&& RegExp.$3<256 && RegExp.$4<256){
									return true
							}
						}
						if(re2.test(value)){
							if(RegExp.$1<256 && RegExp.$2<256
								&& RegExp.$3<256 && RegExp.$4<256 && RegExp.$5<65535){
									return true
							}
						}
						return false;
						
					}
						
					return true;
				},
				msg : "非法地址"
			},
			cast : {
				check : function(value) {
					if(value){
						var re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
						if(re.test(value)){
							if(RegExp.$1>=224 && RegExp.$1<=239
								&& RegExp.$2<256 && RegExp.$3<256 && RegExp.$4<256){
									return true
							}
						}
						return false;
						
					}
						
					return true;
				},
				msg : "非法组播地址"
			},
			iparea : {
				check : function(value) {
					if(value){
						var re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
						if(re.test(value)){
							if(RegExp.$4 == 0){
									return true
							}
						}
						return false;
						
					}
						
					return true;
				},
				msg : "非法网段地址"
			},
			port : {
				check : function(value) {

					if(value){
						var re = /^(\d)+$/;
						if(re.test(value)){
							var tmp = parseInt(value);
							if(tmp > 0 && tmp <=65535){
								return true;
							}
						}
						return false;
					}
					return true;
				},
				msg : "非法网络端口"
			},
			email : {
				check : function(value) {

					if(value)
						return testPattern(value, "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])");
					return true;
				},
				msg : "非法邮件地址"
			},
			url : {

				check : function(value) {

					if(value)
						return testPattern(value, "^https?://(.+\.)+.{2,4}(/.*)?$");
					return true;
				},
				msg : "非法URL地址"
			},
			required : {

				check : function(value) {

					if(value)
						return true;
					else
						return false;
				},
				msg : "不能为空"
			}
		}
		var testPattern = function(value, pattern) {

			var regExp = new RegExp(pattern, "");
			return regExp.test(value);
		}
		return {

			addRule : function(name, rule) {

				rules[name] = rule;
			},
			getRule : function(name) {

				return rules[name];
			}
		}
	}
	/*
	 Form factory
	 */
	var Form = function(form) {

		var fields = [];

		form.find("[validation]").each(function() {
			var field = $(this);
			if(field.attr('validation') !== undefined) {
				fields.push(new Field(field));
			}
		});
		this.fields = fields;
	}
	Form.prototype = {
		validate : function() {

			for(field in this.fields) {

				this.fields[field].validate();
			}
		},
		isValid : function() {

			for(field in this.fields) {

				if(!this.fields[field].valid) {

					this.fields[field].field.focus();
					return false;
				}
			}
			return true;
		}
	}


	function utf8CharLen(str){
		var totalLength = 0; 
		var i; 
		var charCode; 
		for (i = 0; i < str.length; i++) { 
			charCode = str.charCodeAt(i); 
			if (charCode < 0x007f) { 
				totalLength = totalLength + 1; 
			} else if ((0x0080 <= charCode) && (charCode <= 0x07ff)) { 
				totalLength += 2; 
			} else if ((0x0800 <= charCode) && (charCode <= 0xffff)) { 
				totalLength += 3; 
			} 
		} 
		return totalLength; 
	} 
	
	/*
	 Field factory
	 */
	var Field = function(field) {

		this.field = field;
		this.valid = false;
		this.attach("change");
	}
	Field.prototype = {

		attach : function(event) {

			var obj = this;
			if(event == "change") {
				obj.field.bind("change", function() {
					return obj.validate();
				});
			}
			if(event == "keyup") {
				obj.field.bind("keyup", function(e) {
					return obj.validate();
				});
			}
		},
		
		charLenMatch : function(){
			var obj = this;
			var field = obj.field;
			var minLen = -1;
			var maxLen = -1;
			var val = field.val();
			var curLen = utf8CharLen(val); 
			if(typeof(field.attr('minCharLen')) != 'undefined'){
				minLen = parseInt(field.attr('minCharLen'));
				if(minLen > 0 && curLen < minLen){
					return "总字节至少" + minLen + "个";
				}
			}
			if(typeof(field.attr('maxCharLen')) != 'undefined'){
				maxLen = parseInt(field.attr('maxCharLen'));
				if(maxLen > 0 && curLen > maxLen){
					return "总字节超过" + maxLen + "个";
				}
			}
			return "";
		},
		
		lenMatch : function(){
			var obj = this;
			var field = obj.field;
			var minLen = -1;
			var maxLen = -1;
			var val = field.val();
			var curLen = val.length;
			if(typeof(field.attr('minLen')) != 'undefined'){
				minLen = parseInt(field.attr('minLen'));
				if(minLen > 0 && curLen < minLen){
					return "长度至少为" + minLen;
				}
			}
			if(typeof(field.attr('maxLen')) != 'undefined'){
				maxLen = parseInt(field.attr('maxLen'));
				if(maxLen > 0 && curLen > maxLen){
					return "长度最长为" + maxLen;
				}
			}
			return "";
		},
		
		valMatch : function(){
			var obj = this;
			var field = obj.field;
			var minVal = -999999;
			var maxVal = 999999;
			var curVal = parseInt(field.val());
			if(typeof(field.attr('minVal')) != 'undefined'){
				minVal = parseInt(field.attr('minVal'));
				if(curVal < minVal){
					return "值至少为" + minVal;
				}
			}
			if(typeof(field.attr('maxVal')) != 'undefined'){
				maxVal = parseInt(field.attr('maxVal'));
				if(curVal > maxVal){
					return "值最大为" + maxVal;
				}
			}
			return "";
		},
		
		validate : function() {

			var obj = this, 
				field = obj.field, 
				parentGroup = field.parents(".control-group");
				errArea = $(document.createElement("span")).addClass("text-error"),
				types = field.attr("validation").split(" "), 
				container = field.parent(), 
				errorMsg = "";
				
			if(field.is(":hidden")){
				obj.valid = true;
				return ;
			}

			for(var type in types) {
				if(jQuery.trim(types[type]) == ""){
					continue;
				}
				var rule = $.Validation.getRule(types[type]);
				if(!rule.check(field.val())) {
					errorMsg = rule.msg;
					break;
					//errors.push(rule.msg);
				}
			}
			if(!errorMsg){
				errorMsg = obj.charLenMatch();
			}
			if(!errorMsg){
				errorMsg = obj.lenMatch();
			}
			if(!errorMsg){ 
				errorMsg = obj.valMatch();
			}
			container.find(".text-error").each(function() {
				$(this).remove();
			});
			if(errorMsg) {
				obj.field.unbind("keyup")
				obj.attach("keyup");
				parentGroup.addClass("error");
				container.append(errArea.empty());
				errArea.append(errorMsg);
				obj.valid = false;
			} else {
				errArea.remove();
				parentGroup.removeClass("error");
				obj.valid = true;
			}
		}
		
	}

	/*
	 Validation extends jQuery prototype
	 */
	$.extend($.fn, {

		validation : function() {

			var validator = new Form($(this));
			$.data($(this)[0], 'validator', validator);


		},
		validate : function() {

			var validator = $.data($(this)[0], 'validator');
			validator.validate();
			return validator.isValid();

		}
	});
	$.Validation = new Validation();
})(jQuery);

function clearValidateMsg(obj){
	$(obj).find("span.text-error").each(function() {
				$(this).remove();
	});
	$(obj).find("div.control-group").each(function() {
				$(this).removeClass("error");
	});
}
