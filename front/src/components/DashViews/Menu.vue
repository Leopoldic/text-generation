<template>
  <v-container
    fill-height
    fluid
    grid-list-xl>
    <v-layout
      justify-center
      wrap
    >
      <v-flex
        xs12
        md12
      >
        <material-card
          color="#553D80"
          title="Расширенные настройки генерации текста"
          text="Параметры"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <v-flex md4>
                    <v-select
                            :items="model"
                            label="Модель"
                            v-model='mod'
                            @change="filterAuthor"
                    ></v-select>
                </v-flex>

                <v-flex md4>
                    <v-select
                            :items="text_num"
                            label="Кол-во генерируемых текстов"
                            v-model='text_n'
                            @change="filterKurs"
                    ></v-select>
                </v-flex>

                <v-flex md4>
                    <v-text-field
                            label="Кол-во генерируемых слов"
                            @change="donwload_table()"
                            v-model='word_n'
                    ></v-text-field>
                </v-flex>
                  <v-flex md4>
                    <v-select
                            :items="regims"
                            label="Режим"
                            v-model='regim'
                    ></v-select>
                  </v-flex>
                  <v-flex md8 >
                      <v-radio-group
                          v-model="selected"
                          row
                          md12
                          style="align-items: center"
                          >
                          <v-radio
                              label="Расчитать метрику качества BLEU"
                              v-model='not_depth'
                          ></v-radio>
                          <v-radio
                              label="Расчитать метрику качества BLEURT"
                              value="radio-2"
                          ></v-radio>
                      </v-radio-group>
                    </v-flex>
                    <v-flex
                      md12
                      lg12
                    >
                      <material-card
                        class="card-tabs"
                        color="#553D80">
                        <v-flex
                          slot="header"
                        >
                          <v-tabs
                            color="transparent"
                            slider-color="white"
                            v-model="tabs"
                          >
                              <span
                                class="subheading font-weight-light mr-3"
                                style="align-self: center"
                              >Тематические тексты:</span>
                              <v-tab class="mr-3" v-model='tabs'>
                                <v-icon class="mr-2">mdi-bug</v-icon>
                                Добавить
                              </v-tab>
                          </v-tabs>
                        </v-flex>
                        <v-tabs-items v-model="tabs">
                          <v-tab-item
                          >
                          <div>
                            <v-list three-line v-for="(txt,index) in text" :key="txt">
                              <v-list-tile>
                                <v-list-tile-action>
                                  <v-radio-group v-model="selected" >
                                  <v-radio :value="index"
                                  />
                                  </v-radio-group>
                                </v-list-tile-action>
                                <v-list-tile-title>
                                  {{ txt }}
                                </v-list-tile-title>
                              </v-list-tile>
                              <v-divider/>
                            </v-list>
                          </div>
                          </v-tab-item>
                          <v-row align='right'>
                                      <v-btn
                                      color='#553D80'
                                      class="text-none"
                                      depressed
                                      >
                                          <v-icon left>folder</v-icon>
                                          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()">
                                      </v-btn>
                                      <v-dialog flat v-model="dialog1" color="primary" width="500">
                                        <template v-slot:activator="{ on }">
                                          <v-btn color="#356276" dark v-on="on">Написать текст</v-btn>
                                        </template>
                                        <v-card>
                                          <v-card-title color='general'>Подробности выполнения:</v-card-title>
                                        </v-card>
                                        <v-card-text class="black text--darken-3">
                                          <v-form class='px-3'>
                                            <v-text-field :rules="rules" prepend-icon="folder" dark label="Тематический текст:" v-model="comment">
                                            </v-text-field>
                                          </v-form>
                                          <v-btn class='mt-4' color='#356276' @click="apply(); dialog1=false;">Добавить</v-btn>
                                        </v-card-text>
                                      </v-dialog>
                                      <v-btn color="#BBAE50" dark @click="removeElement()">Удалить пункт</v-btn>
                            </v-row>
                        </v-tabs-items>
                      </material-card>
                    </v-flex>
                    <v-flex md6></v-flex>
                    <v-flex md3>
                      <v-btn
                      color='primary'
                      align-end
                      v-if="process_text.length > 0"
                      @click="sendText()"
                      >
                          Генерация тематических текстов
                      </v-btn>
                    </v-flex>
                    <v-flex md2>
                        <v-btn color="primary"
                            dark @click="noText()">
                          Генерация случайных текстов</v-btn>
                    </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>
      <v-flex md6>
        <material-card class="v-card-profile">
          <v-card-title class="text-xs-center">
            <h4 class="card-title font-weight-light"></h4>
            <h3>Обработанные данные</h3>
            <p class="card-description font-weight-light"></p>
          </v-card-title>
          <v-divider></v-divider>
          <material-card v-for="(txt,index) in this.process_text" :key="index">
            <v-card-title>
              <h5>{{"Номер текста: " + index }}</h5>
            </v-card-title>
            <v-textarea
              :value="txt"
              filled
              background-color="grey lighten-2"
              color="cyan"
              readonly
              m10
              >
              </v-textarea>
              <v-flex md12></v-flex>
          </material-card>
        </material-card>
      </v-flex>
      <v-flex md6>
        <material-card class="v-card-profile">
          <v-card-title class="text-xs-center">
            <h4 class="card-title font-weight-light"></h4>
            <h3>Сгенерированный текст(ы)</h3>
            <p class="card-description font-weight-light"></p>
          </v-card-title>
          <v-divider></v-divider>
          <material-card v-for="(txt,index) in this.generated_text" :key="index">
            <v-card-title>
              <h5>{{"Номер текста: " + index }}</h5>
            </v-card-title>
            <v-textarea
              :value="txt"
              filled
              background-color="grey lighten-2"
              color="cyan"
              readonly
              m10
              >
              </v-textarea>
              <v-flex md12></v-flex>
        </material-card>
        </material-card>
      </v-flex>
      <v-flex md6>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
    data: () => ({
        model:['GPT2-small','GPT2-medium','GPT2-large'],
        text_num:[1,2,3,4,5],
        mod:'GPT2-small',
        text_n: 1,
        regims:['CPU','GPU'],
        word_n:30,
        text: [],
        process_text: [],
        upload_docs: [],
        upload_texts: [],
        generated_text: [],
        buf:'',
        content:'',
        comment: '',
        regim:'CPU',
        backgroundColor:'',
        dialog1:false,
        selected:'',
    }),
    methods:{
        delay(ms) {
          return new Promise(r => setTimeout(() => r(), ms))
        },
        removeElement(a){
          this.text.splice(this.selected,1)
          this.process_text.splice(this.selected,1)
          this.selected = ''
        },
        apply(){
          this.text.push('Cозданный текст')
          this.process_text.push(this.comment)
          this.comment = ''
        },
       async handleFileUpload(){
          this.file = this.$refs.file.files[0];
          this.text.push(this.file.name)
          this.file2txt(this.file)
          await this.delay(500)
          this.process_text.push(this.buf)
        },
       async file2txt(file){
          var buf = '';
          let formData = new FormData();
          formData.append('file_uploaded',file);
          axios.
          post( 'http://127.0.0.1:8000/space/upload/',
          formData,
          {
            headers: {
                "Content-Type": 'multipart/form-data',
                'Authorization': 'jwt '.concat(localStorage['token'])
            }
          })
          .then(response  => (
              this.buf = response.data
            ))
        } ,
        sendText(){
          let formData = new FormData();
          formData.append('text',this.process_text.join(' '))
          formData.append('model',this.mod)
          formData.append('text_num',this.text_n)
          formData.append('word_num',this.word_n)
          axios.
          post( 'http://127.0.0.1:8000/space/upload/generate/',
          formData,
          {
            headers: {
                "Content-Type": 'multipart/form-data',
                'Authorization': 'jwt '.concat(localStorage['token'])
            }
          })
          .then(response  => (
              this.generated_text = response.data
            ))
        },
        noText(){
          let formData = new FormData();
          formData.append('text','')
          formData.append('model',this.mod)
          formData.append('text_num',this.text_n)
          formData.append('word_num',this.word_n)
          axios.
          post( 'http://127.0.0.1:8000/space/upload/generate/',
          formData,
          {
            headers: {
                "Content-Type": 'multipart/form-data',
                'Authorization': 'jwt '.concat(localStorage['token'])
            }
          })
          .then(response  => (
              this.generated_text = response.data
            ))
        }
        },
}
</script>