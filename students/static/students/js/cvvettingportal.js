function showContactDetails(phone, email) {
    $('#contactPhone').text(phone);
    $('#contactEmail').text(email);
    $('#contactModal').modal('show');
}

function copyToClipboard(elementId) {
    var text = document.getElementById(elementId).textContent;
    navigator.clipboard.writeText(text).then(function() {
        showTooltip(elementId);
    }, function(err) {
        alert('Failed to copy text: ', err);
    });
}

function showTooltip(elementId) {
    var icon = document.querySelector('#' + elementId + ' ~ .copy-icon');
    $(icon).tooltip({ title: "Copied!", trigger: "manual" }).tooltip('show');
    setTimeout(function() {
        $(icon).tooltip('hide');
    }, 390);
}

$(document).click(function(event) {
    if (!$(event.target).closest('.dropdown').length) {
        $('.dropdown-menu').removeClass('show');
    }
});

function autoRefreshPage() {
    window.location.reload();
}

setInterval(autoRefreshPage, 25000);

document.addEventListener('DOMContentLoaded', function() {
    flatpickr("#datePickerIcon", {
        dateFormat: "Y-m-d",
        defaultDate: new Date(),
        onChange: function(selectedDates, dateStr, instance) {
            filterByDate(dateStr);
        }
    });

    flatpickr("#discrepancyDate", {
        dateFormat: "Y-m-d",
        defaultDate: new Date()
    });

    flatpickr("#discrepancyTime", {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        time_24hr: true
    });

    $('[data-toggle="tooltip"]:not(.copy-icon)').tooltip();
});

function filterByDate(dateStr) {
    window.location.href = "?date=" + dateStr;
}
