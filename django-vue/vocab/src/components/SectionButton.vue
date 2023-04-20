<template>
    <div>
        <div class="sectionGroup">
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(6000,6500)>6000 ~ 6500</button>
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(6500,7000)>6500 ~ 7000</button>
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(6000,7000)>6000 ~ 7000</button>    
        </div>
        <div class="sectionGroup">
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(7000,7500)>7000 ~ 7500</button>
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(7500,8000)>7500 ~ 8000</button>
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(7000,8000)>7000 ~ 8000</button>
        </div>
        <div class="sectionGroup">
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(8000,8500)>8000 ~ 8500</button>
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(8500,9000)>8500 ~ 9000</button>
            <button class="sectionbutton btn btn-primary" v-on:click=toQuizMenu(8000,9000)>8000 ~ 9000</button>
        </div>
    </div>

</template>

<script>
import axios from "axios"

export default {
    name: "SectionButton",
    data() {
        return {
            level3: [6000,6500,7000,7500,8000,8500,9000],

        }
    },
    methods:{
        toQuizMenu:async function(morethan, lessthan){
            
            const resvocabList = await axios.get("http://127.0.0.1:8000/dictionary/dictionary/", {
                params: {
                    more: morethan,
                    less: lessthan
                }
            })
            this.$store.commit('vocabListIn', resvocabList.data)

            const resmeaningList = await axios.get("http://127.0.0.1:8000/dictionary/dictionaryAll/", {})
            this.$store.commit('meaningListIn', resmeaningList.data)

            //↓テスト用json読み込み処理
            // console.log(morethan)
            // console.log(lessthan)
            // const resvocabList = await axios.get("./vocabList.json")
            // this.$store.commit('vocabListIn', resvocabList.data)
            // const resmeaningList = await axios.get("./meaningList.json")
            // this.$store.commit('meaningListIn', resmeaningList.data)

            this.$router.push("/quizmenu")

        }
    }

}
</script>

<style scoped>
.sectionGroup{
    margin:10px;;
}
.sectionbutton{
    margin:4px;
}

</style>