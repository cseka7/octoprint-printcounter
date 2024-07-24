$(function() {
    function PrintCounterViewModel(parameters) {
        var self = this;

        self.resetStatus = ko.observable(false);
        self.filesViewModel = parameters[0]; // Assumes this is the file list view model

        self.resetCounts = function() {
            $.ajax({
                url: "/plugin/printcounter/reset_counts",
                type: "POST",
                success: function(response) {
                    new PNotify({
                        title: 'Print Counter',
                        text: response.message,
                        type: 'success',
                        hide: true
                    });
                    self.resetStatus(true);
                    setTimeout(function() {
                        self.resetStatus(false);
                    }, 3000); // Hide message after 3 seconds
                }
            });
        };

        // Extend file list to include print counts
        self.filesViewModel.files.subscribe(function(files) {
            files.forEach(function(file) {
                if (file.name.endsWith(".gcode")) {
                    var filePath = file.path;
                    $.ajax({
                        url: "/plugin/printcounter/get_count",
                        data: { file_path: filePath },
                        success: function(response) {
                            file.printCount = response.count;
                            // Trigger a manual refresh of the file list to display new data
                            self.filesViewModel.fileListView.refresh();
                        }
                    });
                }
            });
        });
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: PrintCounterViewModel,
        dependencies: ["filesViewModel"],
        elements: ["#file_list"]
    });
});
