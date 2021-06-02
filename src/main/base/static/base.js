const BACKEND_ENDPOINT = '/';

// setting the baseURL for backend API calls
axios.defaults.baseURL = BACKEND_ENDPOINT;
axios.defaults.withCredentials = true

//  intercepting response to handle errors from server
axios.interceptors.response.use(
res => {
    return res;
},
err => {
    console.log('axios error response:', err.response.status);
    switch (err.response.status) {
        case 401: {
            $.message({
                type: 'error',
                text: 'Not authenticated. Please login first!',
                position: 'bottom-center',
            });

            break;
        }

        case 403: {
            $.message({
                type: 'error',
                text: 'Forbidden, please return!',
                position: 'bottom-center',
            });

            break;
        }

        case 404: {
            $.message({
                type: 'error',
                text: 'Resource not found!',
                position: 'bottom-center',
            });

            break;
        }

        case 405: {
            $.message({
                type: 'error',
                text: 'Request method not allowed! [GET, POST...]',
                position: 'bottom-center',
            });

            break;
        }

        case 500: {
            $.message({
                type: 'error',
                text: 'Server confusing to handle!',
                position: 'bottom-center',
            });

            break;
        }
    }

    return Promise.reject(err);
});



/**
 *  The showToast function.
 */
function showToast(text, type, duration=5000) {
    // console.log('showing toast:', text);

    $.message({
        type: type,
        text: text,
        duration: duration,
        position: 'bottom-center',
    });
}


/**
  * Initializing the progressbar.
  */
loadProgressBar({
    speed: 450,
    trickleRate: 0.02,
    trickleSpeed: 1750,
});


/*
 * Setting ajax navigating for a tags that don't have the '' class.
 */
setATagNavigate();
function setATagNavigate() {
    $('a:not(.not-ajax)').each(function(index, elem) {
        $(this).unbind('click').click((e) => {
            e.preventDefault();
            navigateTo($(this).attr('href'));
        });
    });
}


/**
 * Handling on user pressed the Back button on the browser, or even going back by code.
 */
$(window).on("popstate", function (e) {
    console.log('\back pressed:', location.href);
    navigateTo(location.href);

    /*if (e.originalEvent.state !== null) {
        loadAjaxContent(location.href);
    }*/
});


/*
 * Navigating to the desired path by ajax calling.
 */
function navigateTo(path) {
    axios.get(path)
        .then(res => {
            replaceContent(res);
        })
        .catch(err => {
            console.log(err);
        });
}


/**
 * Replacing the #main's innerHTML.
 */
function replaceContent(axiosResponse) {
    const html = axiosResponse.data;
    const path = axiosResponse.request.responseURL;

    // expression: $.parseHTML(data, context = document, keepScripts = false)
    const ajaxContent = $('<div>').append($.parseHTML(html, document, true));
    // console.log('The whole content:', html);
    // console.log('The main content:', ajaxContent.find('#main').html());


    //  replacing html
    $('#main').html(ajaxContent.find('#main').html());
    $('#nav').html(ajaxContent.find('#nav').html());


    //  changing the url bar's content
    window.history.pushState('', '', `${path}`);


    // re-set for new-in a tags
    setATagNavigate();
    setSubmit();
}


/**
 * Setting ajax submit for forms that has the 'ajax' class.
 */
setSubmit();
function setSubmit() {
    $('form.ajax').each(function(index, elem) {
        $(this).submit((e) => {
            e.preventDefault();

            axios.post(e.target.action, new FormData(e.target))
                .then(res => {
                    replaceContent(res);
                })
                .catch(err => {
                    showToast(err.response.data.message, 'error');
                    console.log(err);
                });
        });
    });
}

