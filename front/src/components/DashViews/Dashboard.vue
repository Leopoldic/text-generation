<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
  <v-snackbar
              top="top"
              color="#BBAE50"
              v-model="snackbar"
              general
            >
              <v-icon
                color="white"
                class="mr-3"
              >
                mdi-bell-plus
              </v-icon>
              Обратить внимание:
                <v-list style="background: rgba(204, 204, 204, 0.0);color:white" dense>
                  <v-list-tile
                    v-for="item in notifications"
                    :key="item">
                    <v-list-tile-title>
                      {{ item.rank+ ' '+item.surname+' '+item.name+' '+item.otchestvo+' имеет '+item.narushen+' нарушений.' }}
                    </v-list-tile-title>
                  </v-list-tile>
                </v-list>
              <v-icon
                size="16"
                @click="snackbar = false"
              >
                mdi-close-circle
              </v-icon>
  </v-snackbar>
    <v-layout wrap>
      <v-flex
        md12
        sm12
        lg4
      >
        <material-chart-card
          :data="dailySalesChart.data"
          :options="dailySalesChart.options"
          color="#553D80"
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
        md12
        sm12
        lg4
      >
        <material-chart-card
          :data="emailsSubscriptionChart.data"
          :options="emailsSubscriptionChart.options"
          :responsive-options="emailsSubscriptionChart.responsiveOptions"
          color="#356276"
          type="Bar"
        >
          <h4 class="title font-weight-light">Кол-во разглашений/месяц</h4>
          <p class="category d-inline-flex font-weight-light">
            <v-icon
              color="green"
              small
            >
              mdi-arrow-down
            </v-icon>
            <span class="green--text">7%</span>&nbsp;
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
        md12
        sm12
        lg4
      >
        <material-chart-card
          :data="dataCompletedTasksChart.data"
          :options="dataCompletedTasksChart.options"
          color="#553D80"
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
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="#553D80"
          icon="offline_pin"
          title="Источников проверено"
          :value="table.kur_source.source"
          sub-icon="mdi-calendar"
          sub-text="За все время"
        />
      </v-flex>
      <v-flex
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="#BBAE50"
          icon="mdi-content-copy"
          title="Выявлено нарушений"
          :value="table.fail.narushen"
          sub-icon="mdi-calendar"
          sub-text="За все время"
        />
      </v-flex>
      <v-flex
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="#553D80"
          icon="mdi-information-outline"
          title="Парировано утечек"
          :value="table.fail.fix"
          sub-icon="mdi-calendar"
          sub-text="За все время"
        />
      </v-flex>
      <v-flex
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="#BBAE50"
          icon="face"
          title="Проверено курсантов"
          :value="table.kur_source.kursant"
          sub-icon="mdi-calendar"
          sub-text="За все время"
        />
      </v-flex>
      <v-flex
        md12
        lg6
      >
        <material-card
          color="#356276"
          title="Постоянный | переменный состав академии"
          text="Данные за 2021 год"
        >
          <template>
            <v-layout row wrap>


                <v-flex xs6>
                    <v-select
                            :items="fakultet"
                            label="Факультет"
                            @change="filterAuthor"
                    ></v-select>
                </v-flex>

                <v-flex xs6>
                    <v-select
                            :items="fakultet"
                            label="Курс"
                            @change="filterKurs"
                    ></v-select>
                </v-flex>

                <v-flex xs6>
                    <v-text-field
                            append-icon="search"
                            label="Имя"
                            single-line
                            hide-details
                            @input="filterSearch"
                    ></v-text-field>
                </v-flex>

                <v-flex xs6>
                    <v-text-field
                            append-icon="search"
                            label="Фамилия"
                            single-line
                            hide-details
                            @input="filterSurname"
                    ></v-text-field>
                </v-flex>


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
                            <tr @click="gotoprofile(item.id)">
                                <td>{{ index+1 }}</td>
                                <td class="text-xs-right">{{ item.fakultet }}</td>
                                <td class="text-xs-right">{{ item.kurs }}</td>
                                <td class="text-xs-right">{{ item.name }}</td>
                                <td class="text-xs-right">{{ item.surname }}</td>
                                <td class="text-xs-right">{{ item.rank }}</td>
                            </tr>
                        </template>

                    </v-data-table>

                </v-flex>


            </v-layout>
        </template>
        </material-card>
      </v-flex>
      <v-flex
        md12
        lg6
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
                >Задачи:</span>
                <v-tab class="mr-3" v-model='tabs'>
                  <v-icon class="mr-2">mdi-bug</v-icon>
                  Проверить источник
                </v-tab>
                <v-tab class="mr-3">
                  <v-icon class="mr-2">mdi-code-tags</v-icon>
                  Проверить факультет/курс
                </v-tab>
                <v-tab>
                  <v-icon class="mr-2">mdi-cloud</v-icon>
                  Курсанта
                </v-tab>
            </v-tabs>
          </v-flex>

<!-- --------------------------------------------------000000000000------------------------------------------------------------------------------------ -->
          <v-tabs-items v-model="tabs">
            <v-tab-item
              v-for="n in 3"
              :key="n"
            >
            <div v-if="tabs==0" >
              <v-list three-line v-for="(task,index) in table.tasks" :key="task">
                <v-list-tile>
                  <v-list-tile-action>
                    <!-- <v-checkbox v-model="selected" :value="index"
                     multiple
                    /> -->
                    <v-radio-group v-model="selected" >
                    <v-radio :value="index"
                    />
                    </v-radio-group>
                  </v-list-tile-action>
                  <v-list-tile-title>
                    {{ task.todo }}
                  </v-list-tile-title>
                </v-list-tile>
                <v-divider/>
              </v-list>
            </div>


<!-- ----------------------------------------------------111111111111111------------------------------------------------------------------------------ -->
            <div v-if="tabs==1">
              <v-list three-line v-for="(fak,index) in table.faks_kurs" :key="fak">
                <v-list-tile>
                  <v-list-tile-action>
                  <v-radio-group v-model="selected">
                    <v-radio :value="index"/>
                  </v-radio-group>
                  </v-list-tile-action>
                  <v-list-tile-title>
                    {{ fak.todo }}
                  </v-list-tile-title>
                </v-list-tile>
                <v-divider/>
              </v-list>
            </div>

<!-- ------------------------------------------------------22222222---------------------------------------------------------------------------------- -->
            <div v-if="tabs==2" >
              <v-list three-line v-for="(pers,index) in table.kursant" :key="pers">

                <v-list-tile>
                  <v-list-tile-action>
                    <v-radio-group v-model="selected" >
                    <v-radio :value="index"
                    />
                    </v-radio-group>
                  </v-list-tile-action>
                  <v-list-tile-title>
                    {{ pers.todo }}
                  </v-list-tile-title>
                </v-list-tile>
                <v-divider/>
              </v-list>
            </div>
            </v-tab-item>
            <v-row align='right'>
                        <v-dialog flat v-model="dialog" color="primary" width="500">
                          <template v-slot:activator="{ on }">
                            <v-btn color='#553D80' dark v-on="on">Добавить задачу</v-btn>
                          </template>
                          <v-card>
                            <v-card-title color='general'>Новая задача</v-card-title>
                          </v-card>
                          <v-card-text class="black text--darken-3">
                            <v-form class='px-3'>
                              <v-text-field :rules="rules" prepend-icon="folder" dark label="Задача" v-model="task">
                              </v-text-field>
                            </v-form>
                            <v-btn class='mt-4' color='#553D80' @click="add_task(); close1();">Добавить задачу</v-btn>
                          </v-card-text>
                        </v-dialog>
                        <v-dialog flat v-model="dialog1" color="primary" width="500">
                          <template v-slot:activator="{ on }">
                            <v-btn color="#356276" dark v-on="on">Отметить как выполненное</v-btn>
                          </template>
                          <v-card>
                            <v-card-title color='general'>Подробности выполнения:</v-card-title>
                          </v-card>
                          <v-card-text class="black text--darken-3">
                            <v-form class='px-3'>
                              <v-text-field :rules="rules" prepend-icon="folder" dark label="Комментарий:" v-model="comment">
                              </v-text-field>
                              <v-text-field :rules="rules" prepend-icon="folder" dark label="Насколько успешно выполнена задача:" v-model="uspeh">
                              </v-text-field>
                            </v-form>
                            <v-btn class='mt-4' color='#356276' @click="apply(); close2();">Отметить как выполненное</v-btn>
                          </v-card-text>
                        </v-dialog>
                        <v-dialog flat v-model="dialog2" color="primary" width="500">
                          <template v-slot:activator="{ on }">
                            <v-btn color="#BBAE50" dark v-on="on">Отменить задачу</v-btn>
                          </template>
                          <v-card>
                            <v-card-title color='general'>Подробности выполнения:</v-card-title>
                          </v-card>
                          <v-card-text class="black text--darken-3">
                            <v-form class='px-3'>
                              <v-text-field :rules="rules" prepend-icon="folder" dark label="Комментарий:" v-model="comment">
                              </v-text-field>
                              <v-text-field :rules="rules" prepend-icon="folder" dark label="Причины отмены:" v-model="uspeh">
                              </v-text-field>
                            </v-form>
                            <v-btn class='mt-4' color='#BBAE50' @click="removeElement(); close3();">Отменить задачу</v-btn>
                          </v-card-text>
                        </v-dialog>
              </v-row>
          </v-tabs-items>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      comment:'',
      uspeh:'',
      selected: '',
      task: '',
      check_id: '',
      snackbar: true,
      table:{
        tasks: [],
        faks_kurs:[],
        kursant:[],
        fail:{},
        kur_source:''
      },
      notifications:'',

// _______________________________________________________________Графики_____________________________________________________________________
      dailySalesChart: {
        data: {
          labels: [1,2,3,4,5,6,7,8,9,10,11,12],
          series: [[10,5,15,20,7,12,17,27,10,45,23,19]]
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
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
            [23, 75, 45, 30, 28, 24, 20, 19]
          ]
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 100, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      emailsSubscriptionChart: {
        data: {
          labels: ['Я', 'Ф', 'М', 'A', 'M', 'И', 'И', 'A', 'C', 'О', 'Н', 'Д'],
          series: [[10,5,15,20,7,12,17,27,10,45,23,19]]
        },
        options: {
          axisX: {
            showGrid: false
          },
          low: 0,
          high: 50,
          chartPadding: {
            top: 0,
            right: 5,
            bottom: 0,
            left: 0
          }
        },
        responsiveOptions: [
          ['screen and (max-width: 768x)', {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0]
              }
            }
          }]
        ]
      },
      fakultet:['Все',1,2,3,4,5,6,7,8,9],
      kurs:['Все',1,2,3,4,5],
      filters: {
        search: '',
        fakultet: 'Все',
        kurs: 'Все',
        surname:''
      },
      headers: [
        {
          sortable: true,
          text: 'ID',
          value: 'id'
        },
        {
          sortable: true,
          text: 'Факультет',
          value: 'fak'
        },
        {
          sortable: true,
          text: 'Курс',
          value: 'kurs',
          align: 'right'
        },
        {
          sortable: true,
          text: 'Имя',
          value: 'name',
          align: 'right'
        },
        {
          sortable: true,
          text: 'Фамилия',
          value: 'surname',
          align: 'right'
        },
        {
          sortable: true,
          text: 'Звание',
          value: 'rank',
          align: 'right'
        }
      ],
      items: [],
      tabs: 1,
      list: {
        0: false,
        1: false,
        2: false
      },
      dialog:false,
      dialog1:false,
      dialog2:false
    }
  },
  methods: {
      close1(){
        this.dialog = false
      },
      close2(){
        this.dialog1 = false
      },
      close3(){
        this.dialog2 = false
      },
      cons(){
        console.log(this.selected)
      },

      gotoprofile(id) {
      this.$router.push({ path: `dashboard/user-profile/${id}` });
      },
// ______________________________________МЕТОДЫ ДЛЯ ТАБЛИЦЫ С ЗАДАЧАМИ_____________________________________________
      
      //Задержка для Axios
      delay(ms) {
        return new Promise(r => setTimeout(() => r(), ms))
      },

      //Отмена задачи
      async removeElement() {

        let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
        }

        if(this.tabs === 0 )
        {
        let body = JSON.stringify({
            comment: this.comment,
            uspeh: this.uspeh,
            task: this.table.tasks[this.selected].todo,
            category:'Проверка источника'
            
        })
        axios
        .post('http://127.0.0.1:8000/space/create/task/bad',body,{headers})
        await this.delay(300)
        axios
        .delete('http://127.0.0.1:8000/space/destroy/task/'+this.table.tasks[this.selected].id.toString()+'/',{headers})
        await this.delay(300)
        axios
        .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%98%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA',{headers})
        .then(response => (this.table.tasks = response.data));
        }
        else if(this.tabs === 1 )
        {
        let body_2 = JSON.stringify({
            comment: this.comment,
            uspeh: this.uspeh,
            task: this.table.faks_kurs[this.selected].todo,
            category:'Проверка факультета/курса'
            
        })
        axios
        .post('http://127.0.0.1:8000/space/create/task/bad',body_2,{headers})
        await this.delay(300)
        axios
        .delete('http://127.0.0.1:8000/space/destroy/task/'+this.table.faks_kurs[this.selected].id.toString()+'/',{headers})
        await this.delay(300)
        axios
        .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%A4%D0%B0%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D0%B5%D1%82',{headers})
        .then(response => (this.table.faks_kurs = response.data));
        }
        else if(this.tabs === 2 )
        {
        let body_3 = JSON.stringify({
            comment: this.comment,
            uspeh: this.uspeh,
            task: this.table.kursant[this.selected].todo,
            category:'Проверка курсанта'
            
        })
        axios
        .post('http://127.0.0.1:8000/space/create/task/bad',body_3,{headers})
        await this.delay(300)
        axios
        .delete('http://127.0.0.1:8000/space/destroy/task/'+this.table.kursant[this.selected].id.toString()+'/',{headers})
        await this.delay(300)
        axios
        .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%9A%D1%83%D1%80%D1%81%D0%B0%D0%BD%D1%82',{headers})
        .then(response => (this.table.kursant = response.data));
        }
        this.task = ''
        this.comment = ''
        this.uspeh = ''

      },

      //Добавление задачи
      async add_task() {
        let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
          }
        let body = JSON.stringify({
            todo: this.task,
            category: '',
        })
        if(this.tabs === 0 )
        {
            body = JSON.stringify({
            todo: this.task,
            category: 'Источник',
        })
        }
        else if(this.tabs === 1 )
        {
            body = JSON.stringify({
            todo: this.task,
            category: 'Факультет',
        })
        }
        else if(this.tabs === 2 )
        {
            body = JSON.stringify({
            todo: this.task,
            category: 'Курсант',
        })
        }
        axios
        .post('http://127.0.0.1:8000/space/create/task',body,{headers})
        if(this.tabs === 0 )
        {
        await this.delay(300)
        axios
        .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%98%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA',{headers})
        .then(response => (this.table.tasks = response.data));
        }
        else if(this.tabs === 1 )
        {
        await this.delay(300)
        axios
        .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%A4%D0%B0%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D0%B5%D1%82',{headers})
        .then(response => (this.table.faks_kurs = response.data));
        }
        else if(this.tabs === 2 )
        {
        await this.delay(300)
        axios
        .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%9A%D1%83%D1%80%D1%81%D0%B0%D0%BD%D1%82',{headers})
        .then(response => (this.table.kursant = response.data));
        }
        this.task=''
        this.comment=''
        this.uspeh = ''
      },

      //Выполнение задачи
      async apply() {
        let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
        }
  
        if (this.tabs === 0 )
        { 
          let body = JSON.stringify({
            comment: this.comment,
            uspeh: this.uspeh,
            task:this.table.tasks[this.selected].todo,
            category:'Проверка источника'
            
          })
          axios
          .post('http://127.0.0.1:8000/space/create/task/good',body,{headers})
          await this.delay(300)
          axios
          .delete('http://127.0.0.1:8000/space/destroy/task/'+this.table.tasks[this.selected].id.toString()+'/',{headers});
          await this.delay(300)
          axios
          .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%98%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA',{headers})
          .then(response => (this.table.tasks = response.data));

        }
        else if (this.tabs === 1 )
        {
          let body_2 = JSON.stringify({
            comment: this.comment,
            uspeh: this.uspeh,
            task:this.table.faks_kurs[this.selected].todo,
            category:'Проверка факультета/курса'
            
          })
          axios
          .post('http://127.0.0.1:8000/space/create/task/good',body_2,{headers})
          await this.delay(300)
          axios
          .delete('http://127.0.0.1:8000/space/destroy/task/'+this.table.faks_kurs[this.selected].id.toString()+'/',{headers});
          await this.delay(300)
          axios
          .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%A4%D0%B0%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D0%B5%D1%82',{headers})
          .then(response => (this.table.faks_kurs = response.data));

        }
        else if (this.tabs === 2 )
        { 
          let body_3 = JSON.stringify({
            comment: this.comment,
            uspeh: this.uspeh,
            task:this.table.kursant[this.selected].todo,
            category:'Проверка курсанта'
            
          })
          axios
          .post('http://127.0.0.1:8000/space/create/task/good',body_3,{headers})
          await this.delay(300)
          axios
          .delete('http://127.0.0.1:8000/space/destroy/task/'+this.table.kursant[this.selected].id.toString()+'/',{headers});
          await this.delay(300)
          axios
          .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%9A%D1%83%D1%80%D1%81%D0%B0%D0%BD%D1%82',{headers})
          .then(response => (this.table.kursant = response.data));
        }
        this.task = ''
        this.comment = ''
        this.uspeh = ''
      },

// ______________________________________МЕТОДЫ ДЛЯ ТАБЛИЦЫ С ЛС_______________________________________________________________________________
    //ФИЛЬТРАЦИЯ ТАБЛИЦ
    complete (index) {
      this.list[index] = !this.list[index]
    },
    customFilter(items, filters, filter, headers) {
      // Init the filter class.
      const cf = new this.$MultiFilters(items, filters, filter, headers);

      cf.registerFilter('search', function (searchWord, items) {
        if (searchWord.trim() === '') return items;

        return items.filter(item => {
          return item.name.toLowerCase().includes(searchWord.toLowerCase());
        }, searchWord);

      });

      cf.registerFilter('surname', function (searchWord, items) {
        if (searchWord.trim() === '') return items;

        return items.filter(item => {
          return item.surname.toLowerCase().includes(searchWord.toLowerCase());
        }, searchWord);

      });

      cf.registerFilter('fakultet', function (fakultet, items) {
        if (fakultet === 'Все') return items;

        return items.filter(item => {
          return item.fakultet === fakultet;
        }, fakultet);

      });

      cf.registerFilter('kurs', function (kurs, items) {
        if (kurs === 'Все') return items;

        return items.filter(item => {
          return item.kurs === kurs;
        }, kurs);

      });

      // Its time to run all created filters.
      // Will be executed in the order thay were defined.
      return cf.runFilters();
    },


      /**
       * Handler when user input something at the "Filter" text field.
       */
    filterSearch(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {search: val});
    },

    filterSurname(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {surname: val});
    },

    /**
     * Handler when user  select some author at the "Author" select.
     */
    filterAuthor(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {fakultet: val});
    },

    filterKurs(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {kurs: val});
    }
  },
  // ______________________________________________________________ПЕРЕХОДЫ_________________________________________________________

  // ___________________________________________________________CREATED___________________________________________________________
  created() {
    let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
          }
    axios
      .get('http://127.0.0.1:8000/space/list/kursant',{headers})
      .then(response => (this.items = response.data));
    axios
      .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%98%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA',{headers})
      .then(response => (this.table.tasks = response.data));
      console.log(this.table.tasks)
    axios
      .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%A4%D0%B0%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D0%B5%D1%82',{headers})
      .then(response => (this.table.faks_kurs = response.data));
      console.log(this.table.tasks)
    axios
      .get('http://127.0.0.1:8000/space/list/task?todo=&category=%D0%9A%D1%83%D1%80%D1%81%D0%B0%D0%BD%D1%82',{headers})
      .then(response => (this.table.kursant = response.data));
      console.log(this.table.tasks)
    axios
      .get('http://127.0.0.1:8000/space/sum/fail',{headers})
      .then(response => (this.table.fail = response.data));
    axios
      .get('http://127.0.0.1:8000/space/sum/kurs',{headers})
      .then(response => (this.table.kur_source) = response.data)
    axios
      .get('http://127.0.0.1:8000/space/notification',{headers})
      .then(response => (this.notifications) = response.data)
    
  },
  computed: {
    hasAdditional() {
      return this.additional.length > 0
    }
  }
}
</script>


