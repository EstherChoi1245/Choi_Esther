function validate() {
	var us = document.forms.input.username.value;
	var pd = document.forms.input.password.value; 
	var atPos = us.indexOf("@");
	var dotPos = us.lastIndexOf(".");
	
		
	if((atPos < 1 || dotPos < (atPos + 2))&&(pd.length < 6))
		alert("This is not a valid email address! The password is too short!");
	else {
		if (atPos < 1 || dotPos < atPos + 2) 
			alert("Invalid email address!");
		else if (pd.length < 6)			
			alert("Your password does not meet the minimum requirements!");
		else 
			alert("Success!")


	
	}
	
}