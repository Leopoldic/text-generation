<template>
    
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout
      justify-center
      wrap
    >
    <v-flex md12>
    <material-card>
      <v-layout
      justify-center
      wrap
    >
      <v-flex md6>
          <v-select
                  :items="category"
                  label="Категория"
                  @change="filterAuthor"
          ></v-select>
      </v-flex>


      <v-flex md6>
        <v-text-field
                append-icon="search"
                label="Задача"
                single-line
                hide-details
                @input="filterSearch"
        ></v-text-field>
        </v-flex>
      </v-layout>
    </material-card>
    </v-flex>
      <v-flex
        md12
      >
        <material-card
          color="#356276"
          title="Успешно выполненные задачи"
          text="Данные за 2021 год"
        >
          <template>
            <v-layout row wrap>
                <v-flex xs12>


                    <v-data-table
                            :headers="headers"
                            :items="good"
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
                            <tr @click="selected(item)">
                                <td>{{ index+1 }}</td>
                                <td class="text-xs-left">{{ item.task }}</td>
                                <td class="text-xs-left">{{ item.date }}</td>
                                <td class="text-xs-left">{{ item.category }}</td>
                                <v-btn flat dark v-on="on" @click="dialog=true">
                                  <v-icon color='success'>search</v-icon>
                                </v-btn>
                              </tr>
                        </template>

                    </v-data-table>

                </v-flex>
            </v-layout>
        </template>
        </material-card>
      </v-flex>
      <v-dialog flat v-model="dialog" color="primary" width="500">
                      <v-card>
                        <v-card-title color='general'>Приложение</v-card-title>
                      </v-card>
                      <v-card-text class="black text--darken-3">
                        <v-form class='px-3'>
                          <v-text-field readonly prepend-icon="folder" label="Комментарий:" :value="select.comment"/>
                          <v-text-field readonly prepend-icon="folder" label="Успех:" :value="select.uspeh"/>
                        </v-form>
                        <v-btn class='mt-4' color='general' @click="dialog = false;">Закрыть</v-btn>
                      </v-card-text>
        </v-dialog>
      <v-flex
        md12
      >
        <material-card
          color="#BBAE50"
          title="Отмененные задачи"
          text="Данные за 2021 год"
        >
          <template>
            <v-layout row wrap>

                <v-flex xs12>


                    <v-data-table
                            :headers="headers1"
                            :items="bad"
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
                            <tr @click="selected(item)">
                                <td>{{ index+1 }}</td>
                                <td class="text-xs-left">{{ item.task }}</td>
                                <td class="text-xs-left">{{ item.date }}</td>
                                <td class="text-xs-left">{{ item.category }}</td>
                                <v-btn flat dark v-on="on" @click="dialog2=true">
                                  <v-icon color='red'>search</v-icon>
                                </v-btn>
                            </tr>
                        </template>

                    </v-data-table>

                </v-flex>


            </v-layout>
        </template>
        </material-card>
      </v-flex>
      <v-dialog flat v-model="dialog2" color="primary" width="500">
                      <v-card>
                        <v-card-title color='general'>Приложение</v-card-title>
                      </v-card>
                      <v-card-text class="black text--darken-3">
                        <v-form class='px-3'>
                          <v-text-field readonly prepend-icon="folder" label="Комментарий:" :value="select.comment"/>
                          <v-text-field readonly prepend-icon="folder" label="Причина отмены:" :value="select.uspeh"/>
                        </v-form>
                        <v-btn class='mt-4' color='general' @click="dialog2 = false;">Закрыть</v-btn>
                      </v-card-text>
        </v-dialog>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    headers: [
      {
        sortable: true,
        text: 'ID',
        value: 'id'
      },
      {
        sortable: true,
        text: 'Задача',
        value: 'task'
      },
      {
        sortable: true,
        text: 'Дата выполнения',
        value: 'date'
      },
      {
        sortable: true,
        text: 'Категория',
        value: 'category'
      }
    ],
    headers1: [
      {
        sortable: true,
        text: 'ID',
        value: 'id'
      },
      {
        sortable: true,
        text: 'Задача',
        value: 'task'
      },
      {
        sortable: true,
        text: 'Дата отмены',
        value: 'date'
      },
      {
        sortable: true,
        text: 'Категория',
        value: 'category'
      }
    ],
    dialog:false,
    dialog2:false,
    good:[],
    bad:[],
    category:['Все','Проверка источника', 'Проверка факультета/курса', 'Проверка курсанта'],
    filters: {
        search: '',
        category: 'Все',
      },
    select:{},
  }),
  methods: {
    selected(item){
      this.select = item
      console.log(this.select)
    },

    customFilter(items, filters, filter, headers) {
      // Init the filter class.
      const cf = new this.$MultiFilters(items, filters, filter, headers);

      cf.registerFilter('search', function (searchWord, items) {
        if (searchWord.trim() === '') return items;

        return items.filter(item => {
          return item.task.toLowerCase().includes(searchWord.toLowerCase());
        }, searchWord);

      });

      cf.registerFilter('category', function (category, items) {
        if (category === 'Все') return items;

        return items.filter(item => {
          return item.category === category;
        }, category);

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
    /**
     * Handler when user  select some author at the "Author" select.
     */
    filterAuthor(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {category: val});
    },

  },
  created() {
    let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
          }
    axios
      .get('http://127.0.0.1:8000/space/list/task/good',{headers})
      .then(response => (this.good = response.data));
    axios
      .get('http://127.0.0.1:8000/space/list/task/bad',{headers})
      .then(response => (this.bad = response.data));
  }

}
</script>
