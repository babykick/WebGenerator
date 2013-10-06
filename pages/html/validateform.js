//window.onload = hideAllErrors();

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
  alert("3");
	first_name = document.getElementById("firstname").value;

	last_name = document.getElementById("lastname").value;

	email = document.getElementById("email").value;
	passwd = document.getElementById("passwd").value;
	passwd2 = document.getElementById("passwd2").value;

	if (!checkEmail(email)) {
        hideAllErrors();
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
	} else if (passwd =="" || passwd2=="" || passwd != passwd2 ||
	           passwd.length <6 || passwd.length >16 ) {
		hideAllErrors();
		document.getElementById("pwdError").style.display = "inline";
		document.getElementById("passwd").select();
		document.getElementById("passwd").focus();
		return false;
	} 

	return true;
}

function checkMessageForm(){
    email = document.getElementById("visitor_email").value;
    message = document.getElementById("message").value;

    if (!checkEmail(email)){
         document.getElementById("visitor_email").select();
         document.getElementById("visitor_email").focus();
         alert("Please fill the email in correct format");
         return false;
     }else if(message == ""){
         document.getElementById("message").select();
         document.getElementById("message").focus();
         alert("Please fill the message");
         return false;
     }
    return true;
}

function hideAllErrors() { 
	document.getElementById("nameError").style.display = "none";
	document.getElementById("nameError2").style.display = "none";
	document.getElementById("emailError").style.display = "none";
	document.getElementById("pwdError").style.display = "none";
	document.getElementById("ageError").style.display = "none";

}


function hideAllErrors2() {
	document.getElementById("email").style.display = "none";
	document.getElementById("message").style.display = "none";
}


function checkEmail(inputvalue){	
	var pattern = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return pattern.test(inputvalue);
}
