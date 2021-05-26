const BACKEND_ENDPOINT = 'http://127.0.0.1:5000';

// setting the baseURL for backend API calls
axios.defaults.baseURL = BACKEND_ENDPOINT;

// initializing the progressbar
loadProgressBar({
    trickleSpeed: 1750,
});

setATagNavigate();
function setATagNavigate() {
    $('a').each(function(index, elem) {
        $(this).unbind('click').click((e) => {
            e.preventDefault();
            navigateTo($(this).attr('href'));
        });
    });
}


$(window).on("popstate", function (e) {
    console.log('\back pressed:', location.href);
    navigateTo(location.href);

    /*if (e.originalEvent.state !== null) {
        loadAjaxContent(location.href);
    }*/
});

function navigateTo(path) {
    axios.get(path)
        .then(res => {
            replaceContent(res.data, path);
        })
        .catch(err => {
            console.log(err);
        });
}


// replacing the #main's innerHTML
function replaceContent(html, path) {
    const ajaxContent = $('<div>').append($.parseHTML(html));
    // console.log('The main content:', html.find('#main').html());


    //  replacing html
    $('#main').html(ajaxContent.find('#main').html());
    $('#nav').html(ajaxContent.find('#nav').html());


    //  changing the url bar's content
    window.history.pushState('', '', `${path}`);


    // re-set for new-in a tags
    setATagNavigate();
    setSubmit();
}


setSubmit()
function setSubmit() {
    $('form').each(function(index, elem) {
        $(this).submit((e) => {
            e.preventDefault();

            axios.post(e.target.action, new FormData(e.target))
                .then(res => {
                    replaceContent(res.data, res.request.responseURL);
                })
                .catch(err => {
                    console.log(err);
                });
        });
    });
}
