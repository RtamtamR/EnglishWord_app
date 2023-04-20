import { createStore } from 'vuex'

export default createStore({
  state: {
    vocabList:[],
    meaningList:[]
  },
  getters: {
  },
  mutations: {
    vocabListIn(state,vocabList){
      state.vocabList = vocabList
    },
    meaningListIn(state,meaningList){
      state.meaningList = meaningList
    }
  },
  actions: {
  },
  modules: {
  }
})
