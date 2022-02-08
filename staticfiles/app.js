

// Define a new component called button-counter
Vue.component('button-counter', {
    props: ['car'],
    delimiters: ['[[', ']]'], // This is to avoid issues with django's delimiters
    data: function () {
        return {
        // car:{}
        }
    },
    template: '<div>[[car]]</div>'
})




// injected with Django helper tool
let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], // This is to avoid issues with django's delimiters
    data: {
    hide_list: false,
    year : '',
    make : {id:0, name:'all'},
    model : {id:0, name:'all'},
    models : [],
    makes : [],
    postal : '97223',
    distance : '25',
    results: [],
    }, // end of data

    methods: {
        get_cars : function () {

            axios({
            method: 'get',
            url: `http://localhost:8000/scraper/results/${app.make.id}/${app.model.id}/${app.distance}/${app.postal}/`,
            })
            .then(function (response) {
                app.results = response.data.locations
            });

        },
        get_makes : function () {

            axios({
            method: 'get',
            url: `http://localhost:8000/scraper/makes/`,
            })
            .then(function (response) {
                app.makes = response.data.makes
                
            });

        },
        get_models : function () {

            axios({
            method: 'get',
            url: `http://localhost:8000/scraper/models/`,
            })
            .then(function (response) {
                app.models = response.data.models
            });

        },
        date_splitter : function(string) {
            return string.split('T')[0]
        }
    }, // end of methods
    computed: {
        valid_models: function () {
            // `this` points to the vm instance
            let models = this.models.filter(model_obj => model_obj.makeId === this.make.id)
            models.unshift({id:0,name:'all'})
            return models
    }
    },// end computed
    created: function () {
        this.get_makes()
        this.get_models()
    } // end of created
});
