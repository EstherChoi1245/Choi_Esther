function validate() {
	var us = document.forms.input.username.value;
	var atPos = us.indexOf("@");
	var dotPos = us.lastIndexOf(".");
	var pd = document.forms.input.password.value; 
	
		
	if(atPos < 1 || dotPos < atPos+2 || dotPos+2 > us.length)
		alert("This is not a valid email address!");
	if(pd.length < 6)
		alert("Your password does not meet the minimum requirements!");
	else
		alert("Success!");


	
	}
	
	