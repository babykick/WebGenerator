function checkCheckoutForm(){
    quantity = parseInt(document.getElementById("quantity").value);
    return quantity > 0;
}

function changeQuantity(delta){
    oFormObject = document.forms['checkout_form'];
    oFormElement = oFormObject.elements["quantity"];
    quantity = parseInt(oFormElement.value);
    quantity += delta;
    if(quantity<0) quantity=0;
    oFormElement.value = quantity;
}

function checkRegisterForm() {
	first_name = document.getElementById("firstname").value;
	last_name = document.getElementById("lastname").value;
	email = document.getElementById("email").value;
	passwd = document.getElementById("passwd").value;
	passwd2 = document.getElementById("passwd2").value;
	
	if (!checkEmail(email)) {
		document.getElementById("emailError").style.display = "inline";
		document.getElementById("email").select();
		document.getElementById("email").focus();
		return false;
	}else if (first_name == "")  {
		hideAllErrors();
		document.getElementById("nameError").style.display = "inline";
		document.getElementById("firstname").select();
		document.getElementById("firstname").focus();
		return false;
	}else if (last_name == "")  {
		hideAllErrors();
		document.getElementById("nameError2").style.display = "inline";
		document.getElementById("lastname").select();
		document.getElementById("lastname").focus();
		return false;
	}else if (email == "") {
		hideAllErrors();
		document.getElementById("emailError").style.display = "inline";
		document.getElementById("email").select();
		document.getElementById("email").focus();
		return false;
	} else if (passwd=="" || passwd2=="" || passwd != passwd2 ||
	           passwd.length <6 || passwd.length >16 ) {
		hideAllErrors();
		document.getElementById("pwdError").style.display = "inline";
		document.getElementById("passwd").select();
		document.getElementById("passwd").focus();
		return false;
	} 
	 
	return true;
}

function checkAddressForm(){
    addrline1 = document.getElementById("addrline1").value;
    addrline2 = document.getElementById("addrline2").value;
    city =  addrline2 = document.getElementById("city").value;
    if (addrline1 == "")  {
	 //hideAllErrors();
	 // document.getElementById("addrlineError").style.display = "inline";
	 document.getElementById("addrline1").select();
	 document.getElementById("addrline1").focus();
	 alert("Please fill the address line 1");
	 return false;
     }else if(city == ""){
	 //hideAllErrors();
	// document.getElementById("cityError").style.display = "inline";
	 document.getElementById("city").select();
	 document.getElementById("city").focus();
	 alert("Please fill the city");
	 return false;
     }
}

function hideAllErrors() { 
	document.getElementById("nameError").style.display = "none";
	document.getElementById("nameError2").style.display = "none";
	document.getElementById("emailError").style.display = "none";
	document.getElementById("pwdError").style.display = "none";
	//document.getElementById("addrlineError").style.display = "none";
	//document.getElementById("cityError").style.display = "none";
 
}

function checkEmail(inputvalue){	
	var pattern = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return pattern.test(inputvalue);
}
