'use strict';


class App {

    constructor({
        backendEndpoint = '/',
        scrollTopButton = {
            visible: true,
            offset: 200,
        }
    } = {}) {
        this.backendEndpoint = backendEndpoint;
        this.scrollTopButton = scrollTopButton;

        this.initNProgress();
        this.setAxiosResponseInterceptor();

        if (this.scrollTopButton?.visible) {
            this.setupScrollTopButton();
        }
    }



    initNProgress() {
        /**
         * Initializing the progressbar.
         */
        loadProgressBar({
            speed: 450,
            trickleRate: 0.02,
            trickleSpeed: 1750,
        });
    }

    initAxios() {
        // setting the baseURL for backend API calls
        axios.defaults.baseURL = this.backendEndpoint;
        axios.defaults.withCredentials = true;

        this.setAxiosResponseInterceptor();
    }

    setAxiosResponseInterceptor() {
        //  intercepting response to handle errors from the server or even on the client.
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
            
                    default: {
                        $.message({
                            type: 'error',
                            text: 'Unhanled error! Please check the DevTools Console.',
                            position: 'bottom-center',
                        });
                    }
                }
            
                return Promise.reject(err);
            });
    }

    setupScrollTopButton() {
        console.log(this.scrollTopButton);
    }
}
