#!/usr/bin/node

let app = new Vue({
    el: '#app',
    data () {
        return {
            info: null,
            inform: []
        }
    },
    mounted: function () {

        axios
        .get('http://127.0.0.1:8000/api/v1/search/info')
        .then((res) => {
            this.inform = res.data;
            console.log(res)
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
    }
})
