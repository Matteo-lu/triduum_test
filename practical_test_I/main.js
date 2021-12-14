#!/usr/bin/node

let app = new Vue({
    el: '#app',
    data () {
        return {
            info: null,
            keyword: null,
            loading: true,
            errored: false,
            errors: [],
            results: []
        }
    },
    // mounted () {
    //     axios
    //     .get('http://127.0.0.1:5000/api/v1/courses')
    //     .then(response => {
    //         this.info = response.data.course
    //     })
    //     .catch(error => {
    //         console.log(error)
    //         this.errored = true
    //     })
    //     .finally(() => this.loading = false)
    // },
    methods:{
        checkForm: function (e) {

            if (!this.keyword) {
                this.errors.push("Please enter a keyword to search")
                e.preventDefault();
                this.results = [];
            }

            else {
                this.errors = [];

                var url = "https://en.wikipedia.org/w/api.php"; 
    
                var params = {
                    action: "query",
                    list: "search",
                    srsearch: this.keyword,
                    format: "json"
                };
    
                url = url + "?origin=*";
                Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});
                axios
                .get(url)
                .then((res) => {
                    this.results = res.data.query.search
                })
                .catch((error) => {
                    if (error.response){
                        console.log(error.response)
                        
                    }else if(error.request){
                        console.log(error.request)
                        
                    }else if(error.message){
                        console.log(error.message)
                    }
                });
                e.preventDefault();
            }

        }
    },
})
