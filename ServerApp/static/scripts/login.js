var login = document.forms['form']['login'];
var password = document.forms['form']['password'];

var login_error = document.getElementById('login_error');
var pass_error = document.getElementById('pass_error');


login.addEventListener('textInput', login_Verify);
password.addEventListener('textInput', pass_Verify);

function validated(){
	if (login.value.length < 9) {
		login.style.border = "1px solid red";
		login_error.style.display = "block";
		login.focus();
		return false;
	}
	if (password.value.length < 6) {
		password.style.border = "1px solid red";
		pass_error.style.display = "block";
		password.focus();
		return false;
	}

}
function email_Verify(){
	document.write("test1")
	if (email.value.length >= 8) {
		email.style.border = "1px solid silver";
		email_error.style.display = "none";
		return true;
	}
}
function pass_Verify(){
	if (password.value.length >= 5) {
		password.style.border = "1px solid silver";
		pass_error.style.display = "none";
		return true;
	}
}
