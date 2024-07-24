// octoprint_printcounter/static/js/printcounter.js
$(function() {
    function PrintCounterViewModel(parameters) {
        var self = this;

        self.resetCounts = function() {
            $.ajax({
                url: API_BASEURL + "plugin/printcounter/reset_counts",
                type: "POST",
                success: function(response) {
                    new PNotify({
                        title: 'Print Counts Reset',
                        text: response.message,
                        type: 'success',
                        hide: true
                    });
                },
                error: function() {
                    new PNotify({
                        title: 'Error',
                        text: 'Failed to reset print counts.',
                        type: 'error',
                        hide: true
                    });
                }
            });
        };

        $("#reset_counts_button").click(function() {
            self.resetCounts();
        });
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: PrintCounterViewModel,
        dependencies: [],
        elements: ["#settings_plugin_printcounter"]
    });
});
