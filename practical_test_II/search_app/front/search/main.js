#!/usr/bin/node

let app = new Vue({
    el: '#app',
    data () {
        return {
            info: null,
            loading: true,
            errored: false,
            errors: [],
            results: [],
            post: {
                keyword: null,
                results: null
            }
        }
    },
    methods:{
        checkForm: function (e) {

            if (!this.post.keyword) {
                this.results = [];
            }

            else {
                this.errors = [];

                var url = "https://en.wikipedia.org/w/api.php"; 
    
                var params = {
                    action: "query",
                    list: "search",
                    srsearch: this.post.keyword,
                    format: "json",
                    sroffset: 25
                };

                url = url + "?origin=*";
                Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});
                axios
                .get(url)
                .then((res) => {
                    this.results = res.data.query.search
                    this.post.results = this.results.length
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
                axios
                .post("http://127.0.0.1:8000/api/v1/search", this.post)
                .then((res) => {
                    console.log(res)
                }).catch((error) => {
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
