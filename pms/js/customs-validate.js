$(document).ready(function() {
	
	$("#contactForm").validate({
		rules: {
			yourname: "required",
			contactEmail: {
				required: true,
				email: true
			},
			contactMessage: {
				required: true,
			}
		},
		messages: {
			yourname: "Please enter your firstname",
			contactMessage: {
				required: "Please write your messgae",
				minlength: "Your messgae must consist of at least 50 characters"
			},
			contactEmail: "Please enter a valid email address"
		},
		submitHandler: function(form) {
			$.ajax({
				url : 'mail/contact.php',
				type : 'POST',
				data : {
					name : $('[name="yourname"]').val(),
					email : $('[name="contactEmail"]').val(),
					phone : $('[name="Phone"]').val(),
					comments : $('[name="contactMessage"]').val(),
				},
				beforeSend : function(){
					$('.success_wrapper').hide().empty();
				},
				success : function( result ){
					$('.success_wrapper').show().append( result );
				}
			});
		}
	});
	
});