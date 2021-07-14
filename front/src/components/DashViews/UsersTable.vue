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
      <v-flex md4>
          <v-select
                  :items="fakultet"
                  label="Факультет"
                  @change="filterFak"
          ></v-select>
      </v-flex>

      <v-flex md4>
          <v-select
                  :items="kurs"
                  label="Курс"
                  @change="filterKurs"
          ></v-select>
      </v-flex>

      <v-flex md4>
          <v-select
                  :items="category"
                  label="Результат"
                  @change="filterRes"
          ></v-select>
      </v-flex>

      <v-flex md4>
        <v-text-field
                append-icon="search"
                label="Фамилия"
                single-line
                hide-details
                @input="filterSurname"
        ></v-text-field>
        </v-flex>

      <v-flex md4>
        <v-text-field
                append-icon="search"
                label="Имя"
                single-line
                hide-details
                @input="filterName"
        ></v-text-field>
        </v-flex>
        <v-flex md4>
          <v-text-field
                  append-icon="search"
                  label="Источник"
                  single-line
                  hide-details
                  @input="filterSource"
          ></v-text-field>
        </v-flex>
    </v-layout>
</material-card>
</v-flex>
      <v-flex
        md12
      >
        <material-card
          color="#553D80"
          title="Выполненные проверки"
          text="Данные за 2021 год"
        >
          <template>
            <v-layout row wrap>
                <v-flex xs12>


                    <v-data-table
                            :headers="headers"
                            :items="check"
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
                                <td class="text-xs-left">{{ item.kursant.fakultet }}</td>
                                <td class="text-xs-left">{{ item.kursant.kurs }}</td>
                                <td class="text-xs-left">{{ item.kursant.surname }}</td>
                                <td class="text-xs-left">{{ item.kursant.name }}</td>
                                <td class="text-xs-left">{{ item.source }}</td>
                                <td class="text-xs-left">{{ item.done }}</td>
                                <td class="text-xs-left">{{ item.date }}</td>
                                <v-btn flat dark v-on="on" @click="gotoprofile(item.kursant.id)">
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
      <!-- <v-btn @click="gotofile()" class='general mb-4'>
        Cкачать отчет
      </v-btn> -->
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
        text: 'Факультет',
        value: 'kursant.fakultet'
      },
      {
        sortable: true,
        text: 'Курс',
        value: 'kursant.kurs'
      },
      {
        sortable: true,
        text: 'Фамилия',
        value: 'kursant.surname'
      },
      {
        sortable: true,
        text: 'Имя',
        value: 'kursant.name'
      },
      {
        sortable: true,
        text: 'Источник',
        value: 'source'
      },
      {
        sortable: true,
        text: 'Результат',
        value: 'done'
      },
      {
        sortable: true,
        text: 'Дата',
        value: 'date'
      },
    ],
    dialog:false,
    dialog2:false,
    check:[],
    id:'',
    fakultet:['Все',1,2,3,4,5,6,7,8,9],
    kurs:['Все',1,2,3,4,5],
    filters: {
      fakultet: 'Все',
      kurs: 'Все',
      result: 'Все',
      surname:'',
      name:'',
      source:'',
    },
    category:['Все','Утечка персональных данных', 'Утечка фото/видео', 'Распространение секретных данных','Нарушений не выявлено'],
    select:{},
    result:'',
  }),
  methods: {
    gotofile() {
      axios.
      post( 'http://127.0.0.1:8000/file/get/',
      'привет',
      {
        headers: {
            "Content-Type": 'multipart/form-data',
            'Authorization': 'jwt '.concat(localStorage['token'])
        }
      })
      .then(response => (this.result = response.data))
    },
    delay(ms) {
        return new Promise(r => setTimeout(() => r(), ms))
      },
    gotoprofile(id) {
      console.log(id)
      this.$router.push({ path: `user-profile/${id}` });
      },
    selected(item){
      this.select = item
      console.log(this.select)
    },

    customFilter(items, filters, filter, headers) {
      // Init the filter class.
      const cf = new this.$MultiFilters(items, filters, filter, headers);

      cf.registerFilter('surname', function (searchWord, items) {
        if (searchWord.trim() === '') return items;

        return items.filter(item => {
          return item.kursant.surname.toLowerCase().includes(searchWord.toLowerCase());
        }, searchWord);
      });

      cf.registerFilter('name', function (searchWord, items) {
        if (searchWord.trim() === '') return items;

        return items.filter(item => {
          return item.kursant.name.toLowerCase().includes(searchWord.toLowerCase());
        }, searchWord);
      });

      cf.registerFilter('source', function (searchWord, items) {
        if (searchWord.trim() === '') return items;

        return items.filter(item => {
          return item.source.toLowerCase().includes(searchWord.toLowerCase());
        }, searchWord);
      });

      cf.registerFilter('fakultet', function (fakultet, items) {
        if (fakultet === 'Все') return items;

        return items.filter(item => {
          return item.kursant.fakultet === fakultet;
        }, fakultet);

      });

      cf.registerFilter('kurs', function (kurs, items) {
        if (kurs === 'Все') return items;

        return items.filter(item => {
          return item.kursant.kurs=== kurs;
        }, kurs);

      });

      cf.registerFilter('result', function (result, items) {
        if (result === 'Все') return items;

        return items.filter(item => {
          return item.done === result;
        }, result);

      });

      // Its time to run all created filters.
      // Will be executed in the order thay were defined.
      return cf.runFilters();
    },


      /**
       * Handler when user input something at the "Filter" text field.
       */
    filterSurname(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {surname: val});
    },

    filterName(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {name: val});
    },

    filterSource(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {source: val});
    },
    /**
     * Handler when user  select some author at the "Author" select.
     */
    filterFak(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {fakultet: val});
    },

    filterKurs(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {kurs: val});
    },

    filterRes(val) {
      this.filters = this.$MultiFilters.updateFilters(this.filters, {result: val});
    },

  },
  async created() {
    let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
          }
    axios
      .get('http://127.0.0.1:8000/space/list/check',{headers})
      .then(response => (this.check = response.data));
  }

}
</script>