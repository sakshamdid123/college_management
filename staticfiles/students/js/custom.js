$(document).ready(function() {
    function resetModal() {
        $('#changeOption').val('');
        $('#phoneFields').addClass('d-none');
        $('#emailFields').addClass('d-none');
        $('#newPhone').val('');
        $('#newEmail').val('');
    }

    $('#changeContactModal').on('shown.bs.modal', function () {
        resetModal();
    });

    // Dynamically handle search suggestions and results
    $('#student_id').on('input', function() {
        let query = $(this).val();
        if (query) {
            $.ajax({
                url: '/students/search_suggestions/',
                data: {'q': query},
                success: function(data) {
                    let suggestionsBox = $('#suggestions');
                    suggestionsBox.empty();
                    data.suggestions.forEach(function(item) {
                        suggestionsBox.append(`<div class="suggestion" data-id="${item.student_id}">${item.student_id} - ${item.student_name}</div>`);
                    });

                    $('#student-list').html(data.html);
                }
            });
        } else {
            $('#suggestions').empty();
            $.ajax({
                url: '/students/search_suggestions/',
                data: {'q': ''},
                success: function(data) {
                    $('#student-list').html(data.html);
                }
            });
        }
    });

    // Event delegation for dynamically added change-contact buttons
    $(document).on('click', '.change-contact', function() {
        let studentId = $(this).data('id');
        let studentName = $(this).data('name');
        let phone = $(this).data('phone');
        let email = $(this).data('email');

        $('#changeContactModal').modal('show');
        $('#changeContactModalLabel').text(`Change Contact Details for ${studentName}`);
        $('#oldPhone').val(phone);
        $('#oldEmail').val(email);
        $('#changeContactForm').data('student-id', studentId);
    });

    $('#changeOption').on('change', function() {
        let option = $(this).val();
        if (option === 'phone') {
            $('#phoneFields').removeClass('d-none');
            $('#emailFields').addClass('d-none');
        } else {
            $('#phoneFields').addClass('d-none');
            $('#emailFields').removeClass('d-none');
        }
    });

    $('#changeContactForm').on('submit', function(e) {
        e.preventDefault();
        let studentId = $(this).data('student-id');
        let option = $('#changeOption').val();
        let newValue = option === 'phone' ? $('#newPhone').val() : $('#newEmail').val();
        $.ajax({
            url: '/students/update_contact/',
            method: 'POST',
            data: {
                'student_id': studentId,
                'option': option,
                'new_value': newValue,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(response) {
                $('#changeContactModal').modal('hide');
                alert('Contact details updated successfully!');
                window.location.reload();
            },
            error: function() {
                alert('An error occurred. Please try again.');
            }
        });
    });
});


$(document).ready(function() {
    // Function to attach event listeners for change contact functionality
    function attachChangeContactListeners() {
        // Your existing event listeners for change contact functionality
        $('.change-contact-btn').on('click', function() {
            var studentId = $(this).data('student-id');
            // Fetch and populate the change contact modal
            // Assuming you have a function to do this
            fetchAndPopulateChangeContactModal(studentId);
            $('#changeContactModal').modal('show');
        });
    }

    // Initial attachment of event listeners
    attachChangeContactListeners();

    // Search suggestions event
    $('#student_id').on('input', function() {
        var query = $(this).val();
        $.ajax({
            url: "{% url 'search_suggestions' %}",
            method: "GET",
            data: { q: query },
            success: function(response) {
                $('#suggestions').html(response.html);
                // Reattach event listeners after updating the student list
                attachChangeContactListeners();
            },
            error: function(xhr, status, error) {
                console.log('Error: ' + error);
            }
        });
    });
});
