function welcome_header() {
    echo "Welcome to the teflo demo script!"
}

function teflo_header() {
    echo "Starting teflo.."
    echo ""
}

function enable_teflo_virt_env() {
    echo "Please provide the location to your teflo virtual environment:"
    read teflo_virt_env
    echo "Enabling teflo virtual environment: ${teflo_virt_env}"
    source "${teflo_virt_env}/bin/activate"
    teflo --version
}

function teflo_run() {
    teflo_header
    teflo run -t $1 -s $2
}

function teflo_provision() {
    teflo_header
    teflo run -t "validate" \
    -t "provision" \
    -s "scenario.yml"
}

function teflo_orchestrate() {
    teflo_header
    teflo run -t "validate" \
    -t "provision" \
    -t "orchestrate" \
    -s "scenario.yml"
}

function teflo_cleanup() {
    teflo_header
    teflo run -t "cleanup" \
    -s ".teflo/.results/results.yml" \
    -w .
}

function teflo_execute() {
    teflo_header
    teflo run -t "validate" \
    -t "provision" \
    -t "execute" \
    -s "scenario.yml"
}
