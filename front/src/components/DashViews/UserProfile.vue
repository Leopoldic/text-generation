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
        md8
      >
        <material-card
          color="#553D80"
          title="Профиль курсанта"
          text="Статистика нарушений"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Факультет"
                    :value="this.props.fakultet"
                    readonly/>
                </v-flex>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Курс"
                    :value="this.props.kurs"
                    readonly
                  />
                </v-flex>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Группа"
                    :value="this.props.teach_group"
                    readonly
                    />
                </v-flex>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Фамилия"
                    :value="this.props.surname"
                    readonly
                    />
                </v-flex>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Имя"
                    :value="this.props.name"
                    readonly
                    />
                </v-flex>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Отчество"
                    :value="this.props.otchestvo"
                    readonly
                    />
                </v-flex>
                <v-flex
                  xs12
                  md6
                >
                  <material-stats-card
                    color="#5E34AA"
                    icon="mdi-information-outline"
                    title="Нарушений"
                    :value="this.props.narushen"
                    sub-icon="mdi-calendar"
                    sub-text="За весь период обучения"
                  />
                </v-flex>
                <v-flex
                  xs12
                  md6
                >
                  <material-stats-card
                    color="#BBAE50"
                    icon="offline_pin"
                    title="Утечек предотвращено"
                    :value="this.props.fix"
                    sub-icon="mdi-calendar"
                    sub-text="За весь период обучения"
                  />
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>
      <v-flex
        xs12
        md4
      >
        <material-card class="v-card-profile">
          <v-avatar
            slot="offset"
            class="mx-auto d-block"
            size="268"
          >
            <v-icon size="130" color="#553D80">face</v-icon>
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h4 class="card-title font-weight-light">{{ this.props.name + ' ' + this.props.surname + ' ' + this.props.otchestvo}}</h4>
            <h5 class="grey--text">Характеристика</h5>
            <p class="card-description font-weight-light">{{ this.props.charact}}</p>
            <v-btn
              color="#553D80"
              round
              class="font-weight-light"
              @click="dialog=true"
            >Проверить</v-btn>
          </v-card-text>
        </material-card>
      </v-flex>
      <v-dialog flat v-model="dialog" class="indigo lighten-4" width="700">
                      <v-card>
                        <v-card-title class='indigo darken-2'>Меню проверки</v-card-title>
                      </v-card>
                      <v-card-text class='indigo lighten-4' align="center">
                        <v-col cols="12">
                          <v-select
                            :items="['Учебный','Реальный']"
                            :menu-props="{ top: false, offsetY: true }"
                            label="Выберите режим"
                            color='general'
                            v-model="choice"
                          ></v-select>
                        </v-col>
                      </v-card-text>
                      <v-card-text class="indigo lighten-4 text--darken-3" v-if="choice=='Учебный'">
                        <v-form>
                          <v-icon>folder</v-icon>
                          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
                        </v-form>
                        <v-btn class='mt-4' color='general' @click="submitFile(); dialog=false; dialog1=true">Проверить</v-btn>
                      </v-card-text>
                      <v-card-text class="indigo lighten-4 text--darken-3" v-if="choice=='Реальный'">
                        <v-form>
                          <v-text-field :rules="rules" prepend-icon="folder" label="Введите адрес источника:" v-model="source">
                              </v-text-field>
                        </v-form>
                        <v-btn class='mt-4' color='general' @click="submitUrl(); dialog=false; dialog1=true">Проверить</v-btn>
                      </v-card-text>
        </v-dialog>
        <v-dialog flat v-model="dialog1" color="primary" width="700">
                      <v-card>
                        <v-card-title class='indigo darken-2'>Результат проверки</v-card-title>
                      </v-card>
                      <v-card-text class="indigo lighten-4 text--darken-3">
                        <v-form>
                          <v-text-field color='red' readonly :value="this.result['res']">
                          </v-text-field>
                          <v-card v-if="this.result['res'] === 'Выявлено нарушение: Утечка персональных данных'">
                            <span>Фамилия Имя Отчество:</span>
                            <div>
                              <span style='background-color:red'>{{this.result['pers']}}</span>
                            </div>
                            <span>Организации:</span>
                            <div v-for="org in this.result['org']" :key="org">
                              <span style='background-color:orange'> {{ org }} </span>
                            </div>
                            <span>Местоположение:</span>
                            <div v-for="loc in this.result['loc']" :key="loc">
                              <span style='background-color:blue' class='white--text'> {{ loc }} </span>
                            </div>
                            <span>Извлеченный текст:</span>
                            <v-card-text>
                              {{ this.result['text']}}
                            </v-card-text>
                          </v-card>
                        </v-form>
                        <v-btn class='mt-4' color='general' @click="go_to_null(); dialog1=false">Закрыть</v-btn>
                      </v-card-text>
        </v-dialog>
      <v-flex
        md4
        sm12
      >
        <material-chart-card
          :data="dailySalesChart.data"
          :options="dailySalesChart.options"
          color="#5E34AA"
          type="Line"
        >
          <h4 class="title font-weight-light">Статистика нарушений за месяц</h4>
          <p class="category d-inline-flex font-weight-light">
            <v-icon
              color="green"
              small
            >
              mdi-arrow-down
            </v-icon>
            <span class="green--text">9%</span>&nbsp;
            Уменьшилось в этом месяце
          </p>

          <template slot="actions">
            <v-icon
              class="mr-2"
              small
            >
              mdi-clock-outline
            </v-icon>
            <span class="caption grey-lighten-1--text font-weight-light">обновлено 5 часов назад</span>
          </template>
        </material-chart-card>
      </v-flex>
      <v-flex
        md4
        sm12
      >
        <material-chart-card
          :data="dataCompletedTasksChart.data"
          :options="dataCompletedTasksChart.options"
          color="#5E34AA"
          type="Line"
        >
          <h4 class="title font-weight-light">Парирование утечек/месяц</h4>
          <p class="category d-inline-flex font-weight-light">
            <v-icon
              color="green"
              small
            >
              mdi-arrow-down
            </v-icon>
            <span class="green--text">3%</span>&nbsp;
            Уменьшилось в этом месяце
          </p>

          <template slot="actions">
            <v-icon
              class="mr-2"
              small
            >
              mdi-clock-outline
            </v-icon>
            <span class="caption grey-lighten-1--text font-weight-light">обновлено 7 часов назад</span>
          </template>
        </material-chart-card>
      </v-flex>
       <v-flex
        md4
        sm12
      >
        <material-card
          color="#BBAE50"
          title="Нарушения: за все время"
          text="Данные за 2021 год"
        >
          <template>
            <v-layout row wrap>
                <v-flex xs12>


                    <v-data-table
                            :headers="headers"
                            :items="items"
                            item-key="name"
                            class="elevation-1"

                            :search="filters"
                            :custom-filter="customFilter"
                    >
                        <template
                          slot="headerCell"
                          slot-scope="{ header }"
                        >
                          <span
                            class="font-weight-light text-warning text--darken-3"
                            v-text="header.text"
                          />
                        </template>

                        <template slot="items"
                        slot-scope="{ index, item }"
                        >
                            <tr>
                                <td>{{ index+1 }}</td>
                                <td class="text-center">{{ item.done }}</td>
                                <td class="text-center">{{item.date}}</td>
                            </tr>
                        </template>

                    </v-data-table>

                </v-flex>


            </v-layout>
        </template>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      dialog: false,
      dialog1:false,
      source:'',
      file:'',
      id:'',
      choice:'',
      result:' ',
      props: {},
      items: [],
      dailySalesChart: {
        data: {
          labels: [1,2,3,4,5,6,7,8,9,10,11,12],
          series: [[2,1,4,0,3,1,5,2,3,4,5,0,1]]
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 10, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      dataCompletedTasksChart: {
        data: {
          labels: ['Я', 'Ф', 'М', 'А', 'М', 'И', 'И', 'А'],
          series: [
            [1, 2, 0, 3, 0, 2, 1, 3]
          ]
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 10, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      headers: [
        {
          sortable: true,
          text: 'ID',
          value: 'id',
        },
        {
          sortable: true,
          text: 'Нарушение',
          value: 'done',
        },
        {
          sortable: true,
          text: 'Дата',
          value: 'date',
        },
      ],
    }
  },
  created() 
  {
    localStorage.setItem('id', '')
    localStorage.setItem('id', this.$router.currentRoute.params.id)
    console.log(localStorage)
    let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
          }

    this.id = this.$router.currentRoute.params.id
    console.log(localStorage['token'])
    axios
    .get(`http://127.0.0.1:8000/space/retrieve/kursant/${this.id}/`,{headers})
    .then(response => (this.props = response.data));
    axios
    .get(`http://127.0.0.1:8000/space/list/fail?kursant=${this.id}`,{headers})
    .then(response => (this.items = response.data));
  },
  methods:{
    go_to_null(){
      this.result=''

    },

    delay(ms) {
        return new Promise(r => setTimeout(() => r(), ms))
      },
    download_new(){
      localStorage.setItem('id', '')
      localStorage.setItem('id', this.$router.currentRoute.params.id)
      console.log(localStorage)
      let headers = {
          'Content-Type': 'application/json',
          'Authorization': 'jwt '.concat(localStorage['token'])
            }

      this.id = this.$router.currentRoute.params.id
      console.log(localStorage['token'])
      axios
      .get(`http://127.0.0.1:8000/space/retrieve/kursant/${this.id}/`,{headers})
      .then(response => (this.props = response.data));
      axios
      .get(`http://127.0.0.1:8000/space/list/fail?kursant=${this.id}`,{headers})
      .then(response => (this.items = response.data));
    },

    handleFileUpload(){
      this.file = this.$refs.file.files[0];
    },
    async submitFile(){
      console.log(this.file.name)
      let formData = new FormData();
      formData.append('name',this.props.name+' '+this.props.surname+' '+this.props.otchestvo);
      formData.append('id',this.props.id);
      formData.append('source',this.file.name);
      formData.append('file_uploaded',this.file);
      // var object = {};
      // formData.forEach(function(value, key){
      //     object[key] = value;
      // });
      // var json = JSON.stringify(object);
      // var json = JSON.stringify(formData);
      axios.
      post( 'http://127.0.0.1:8000/file/upload/',
      formData,
      {
        headers: {
            "Content-Type": 'multipart/form-data',
            'Authorization': 'jwt '.concat(localStorage['token'])
        }
      })
      .then(response => (this.result = response.data))
      await this.delay(300)
      this.download_new()

    } ,
    submitUrl(){
      let body = JSON.stringify({
        name:this.props.name+' '+this.props.surname+' '+this.props.otchestvo,
        id:this.props.id,
        source: this.source
      })
      let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
        }
      axios
      .post('http://127.0.0.1:8000/file/uploadurl/',body,{headers})
      .then(response => (this.result=response.data))
      this.download_new

      

    }
  }

}
</script>
