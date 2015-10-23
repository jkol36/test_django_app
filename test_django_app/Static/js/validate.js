

function validateForm(e) {
	console.log(e)
	console.log("called");
    var x = document.forms["signupForm"]["first_name"].value;
    if (x == null || x == "") {
        alert("first_name must be filled out");
        return false;
    }
}