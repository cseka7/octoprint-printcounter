// static/js/printcounter.js
$(function() {
    function PrintCounterViewModel(parameters) {
        var self = this;

        self.files = parameters[0].listHelper.allItems;

        self.files.subscribe(function(files) {
            files.forEach(function(file) {
                if (file.type === "machinecode") {
                    // Assuming print_counts is a global variable containing print counts
                    var count = print_counts[file.name] || 0;
                    file.print_count = count;
                }
            });
        });
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: PrintCounterViewModel,
        dependencies: ["fileListViewModel"],
        elements: ["#files"]
    });
});
