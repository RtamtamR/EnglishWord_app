<template>
    <div class="QuizView">
        <div class="Accuracy">
            {{ this.textCorrect }} / {{ this.index }}
        </div>
        
        <div class="Target">
            {{ this.textTarget }}
        </div>
        <div class="pronounce">
            {{ this.targetPronounce }}
        </div>
        
        <div class="answerSvg">
            <img v-show="circleShowFlg" src="../assets/circle.svg">
            <img v-show="closeShowFlg" src="../assets/close.svg">
        </div>

        <div class="Section">
            <button v-show="sectionShowFlg" v-on:click="OnClickSection(0)" class="section btn" 
                    v-bind:class="
                        {'btn-light':this.sec0Corr === 0,
                        'btn-outline-danger':this.sec0Corr === 1,
                        'btn-outline-primary':this.sec0Corr === 2}">
                    {{ this.textSection0 }}
            </button>
        </div>
        <div class="Section">
            <button v-show="sectionShowFlg" v-on:click="OnClickSection(1)" class="section btn" 
                    v-bind:class="
                        {'btn-light':this.sec1Corr === 0,
                        'btn-outline-danger':this.sec1Corr === 1,
                        'btn-outline-primary':this.sec1Corr === 2}">
                    {{ this.textSection1 }}
            </button>
        </div>
        <div class="Section">
            <button v-show="sectionShowFlg" v-on:click="OnClickSection(2)" class="section btn" 
                    v-bind:class="
                        {'btn-light':this.sec2Corr === 0,
                        'btn-outline-danger':this.sec2Corr === 1,
                        'btn-outline-primary':this.sec2Corr === 2}">
                    {{ this.textSection2 }}
            </button>
        </div>
        <div class="Section">
            <button v-show="sectionShowFlg" v-on:click="OnClickSection(3)" class="section btn" 
                    v-bind:class="
                        {'btn-light':this.sec3Corr === 0,
                        'btn-outline-danger':this.sec3Corr === 1,
                        'btn-outline-primary':this.sec3Corr === 2}">
                    {{ this.textSection3 }}
            </button>
        </div>

        <div class="ShowNext">
            <button v-show="showbtnShowFlg" v-on:click="OnClickShowBtn()" class="showbtn btn btn-primary">
                    <label>SHOW &nbsp; CHOICE</label>
            </button>
            <button v-show="nextbtnShowFlg" v-on:click="OnClickNextBtn()" class="nextbtn btn btn-success">
                    <label>NEXT &nbsp; &nbsp; &nbsp; &nbsp; >>>> &nbsp; &nbsp;</label>
            </button>
        </div>
    </div>
</template>

<script>


export default {
    name: "QuizView",
    data() {
        return {
            vocabList:[],
            meaningList:[],
            // ----- 以下、表示/非表示フラグ ------
            sectionShowFlg:false,
            showbtnShowFlg:true,
            nextbtnShowFlg:false,
            circleShowFlg:false,
            closeShowFlg:false,

            // section正負状態プロパティ値 BoostrapのButtonクラス
            // 0 = btn-light(通常)
            // 1 = btn-danger(正解)
            // 2 = btn-primary(不正解)
            sec0Corr:0,
            sec1Corr:0,
            sec2Corr:0,
            sec3Corr:0,

            // 表示テキスト要素
            textIndex:1,
            textCorrect:0,
            
            textTarget:"",
            targetPronounce:"",

            textSection0:"",
            textSection1:"",
            textSection2:"",
            textSection3:"",

            // 単語リストのindex
            index:0,

            // 正解のSectionの場所
            correctSection:0,

        }
    },
    methods: {
        OnClickShowBtn:function(){
            // 非表示要素を表示に
            this.sectionShowFlg = true

            // 表示要素を非表示に
            this.showbtnShowFlg = false

            // ここで初回のみ初期化処理 window.onload()じゃstoreにアクセスできなかった
            if(this.index == 0){
                this.InitializeList()
            }

        },
        InitializeList:function(){
            // storeに保存したリストを取り出す
            this.vocabList = this.$store.state.vocabList
            this.meaningList = this.$store.state.meaningList

            
            // リストをランダムに並び替える
            for(let i = (this.vocabList.length - 1); 0 < i; i--){
                let r = Math.floor(Math.random() * (i + 1))

                let tmp = this.vocabList[i]
                this.vocabList[i] = this.vocabList[r]
                this.vocabList[r] = tmp

            }

            // 問題をセット
            this.SetSection()
        },
        OnClickSection:function(sectionNum){

            // Nextボタンを表示
            this.nextbtnShowFlg = true

            // 選択肢のスタイルを初期化
            this.InitializeSectionStyle()

            if(this.correctSection == sectionNum){
                // 正解処理
                this.IfCorrect(sectionNum)

            }else{
                // 不正解処理
                this.IfInCorrect(sectionNum)

            }

        },
        IfCorrect:function(sectionNum){
            // 〇を画面に表示 / ×を非表示
            this.circleShowFlg = true
            this.closeShowFlg = false

            // 選択肢のスタイルを変化
            switch(sectionNum){
                case 0:
                    this.sec0Corr = 1
                    break
                case 1:
                    this.sec1Corr = 1
                    break
                case 2:
                    this.sec2Corr = 1
                    break
                case 3:
                    this.sec3Corr = 1
                    break
            }

            // 正解数 / 問題数 の正解数を+1
            this.textCorrect++

        },
        IfInCorrect:function(sectionNum){
            // ×を画面に表示 / 〇を非表示
            this.closeShowFlg = true
            this.circleShowFlg = false

            // 選択した選択肢のスタイルを変化
            switch(sectionNum){
                case 0:
                    this.sec0Corr = 2
                    break
                case 1:
                    this.sec1Corr = 2
                    break
                case 2:
                    this.sec2Corr = 2
                    break
                case 3:
                    this.sec3Corr = 2
                    break
            }

            // 正解の選択肢をbtn-dangerスタイルに
            switch(this.correctSection){
                case 0:
                    this.sec0Corr = 1
                    break
                case 1:
                    this.sec1Corr = 1
                    break
                case 2:
                    this.sec2Corr = 1
                    break
                case 3:
                    this.sec3Corr = 1
                    break
            }


        },
        OnClickNextBtn:function(){
            // 問題更新
            this.SetSection()

            // 選択肢のスタイルを初期化
            this.InitializeSectionStyle()

            // 表示要素切り替え
            this.nextbtnShowFlg = false
            this.sectionShowFlg = false
            this.circleShowFlg = false
            this.closeShowFlg = false
            this.showbtnShowFlg = true


        },
        SetSection:function(){

            // 問題をすべて解いたらアラート
            if(this.index == this.vocabList.length){
                alert("すべての問題を解きました")
                return
            }

            // 問題文に対象の単語と発音をセット
            this.textTarget = this.vocabList[this.index].vocab
            this.targetPronounce = this.vocabList[this.index].pronounce

            // 正解を置く場所をランダムに決める ( 0 ~ 3 )
            this.correctSection =  Math.floor(Math.random() * 4)

            // 正解のセクションに意味をセット / ほかの場所(不正解)はmeaningListからランダムに埋める
            switch(this.correctSection) {
                case 0:
                    this.textSection0 = this.vocabList[this.index].meaning

                    this.textSection1 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection2 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection3 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    
                    break

                case 1:
                    this.textSection1 = this.vocabList[this.index].meaning

                    this.textSection0 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection2 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection3 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    
                    break

                case 2:
                    this.textSection2 = this.vocabList[this.index].meaning

                    this.textSection0 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection1 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection3 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning

                    break

                case 3:
                    this.textSection3 = this.vocabList[this.index].meaning

                    this.textSection0 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection1 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    this.textSection2 = this.meaningList[Math.floor(Math.random() * this.meaningList.length)].meaning
                    
                    break
            }

            // indexを進める
            this.index++
        
        },
        InitializeSectionStyle:function(){
            this.sec0Corr = 0
            this.sec1Corr = 0
            this.sec2Corr = 0
            this.sec3Corr = 0
        }

    }
}

</script>


<style scoped>

.QuizView {
    text-align:center;
}

.Accuracy {
    text-align: center;
}

.Target {
    font-size:40px;
    margin:5px 5px 0px 5px;
    text-align: center;
}

.pronounce {
    margin-bottom: 5px;
    text-align: center;
}

.Section {
    position:relative;
    text-align:center;
    z-index: 0;
}
.section {
    margin:10px;
    width:80%;
    height:55px;
    text-align:center;
}

.ShowNext {
    display:inline-block;
    margin-top:20px;
}

.showbtn {
    margin-top:290px;
    width: 300px;
    height: 60px;
    font-size: 20px;
}
.nextbtn {
    width: 300px;
    height: 60px;
    font-size: 20px;
    text-align:right;
}

.answerSvg {
    /* 要素を重ねた時の順番 */
    z-index:1;

    /* 画面全体を覆う設定 */
    position:fixed;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    width:100px;
    height:100px;

    /* 画面の中央に要素を表示させる設定 */
    display: flex;
    align-items: center;
    justify-content: center;

    /* 後ろの要素をクリックできるように */
    pointer-events: none;

    /* 透過 */
    opacity: 0.6;
}

</style>

