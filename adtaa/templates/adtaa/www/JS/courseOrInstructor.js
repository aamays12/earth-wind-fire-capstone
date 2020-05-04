$("#instructorDiv").hide();
$("#courseDiv").hide();
$("#courseOrInstructor").change(function () {
		if($(this).val() == "instructor") {
			$('#instructorDiv').show();
			$('#instructorForm').attr('required', '');
			$('#instructorForm').attr('data-error', 'This field is required.');
		} else {
			$('#instructorDiv').hide();
			$('#instructorForm').removeAttr('required');
			$('#instructorForm').removeAttr('data-error');
		}
		if($(this).val() == "course") {
			$('#courseDiv').show();
			$('#courseForm').attr('required', '');
			$('#courseForm').attr('data-error', 'This field is required.');
		} else {
			$('#courseDiv').hide();
			$('#courseForm').removeAttr('required');
			$('#courseForm').removeAttr('data-error');
		}
});
$("#courseOrInstructor").trigger("change");