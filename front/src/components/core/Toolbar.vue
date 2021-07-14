<template>
  <v-toolbar
    id="core-toolbar"
    app
    color="#404980"
    flat
    prominent>
    <div class="v-toolbar-title">
      <v-toolbar-title class="font-weight-light text-general">
        <v-btn
          v-if="responsive"
          class="default v-btn--simple"
          icon
          @click.stop="onClickBtn">
          <v-icon>mdi-view-list</v-icon>
        </v-btn>
      </v-toolbar-title>
    </div>
    <v-dialog flat v-model="dialog" width="700">
                      <v-card>
                        <v-card-title class='indigo darken-2 white--text'>Настройка сервиса</v-card-title>
                        <v-subheader>Кол-во ежедневных проверок</v-subheader>
                          <v-card-text class="pt-0">
                            <v-slider
                              v-model="value"
                              :rules="rules"
                              label="Число проверок"
                              step="1"
                              thumb-label="always"
                              ticks
                            ></v-slider>
                          </v-card-text>
                          <v-card-text class="pt-0">
                            <v-slider
                              v-model="value1"
                              :rules="rules1"
                              label="Число сканирований в минуту"
                              step="1"
                              thumb-label="always"
                              ticks
                            ></v-slider>
                          </v-card-text>
                          <v-card-text class="pt-0">
                            <v-slider
                              v-model="value2"
                              :rules="rules2"
                              label="Число используемых ядер"
                              step="1"
                              thumb-label="always"
                              ticks
                            ></v-slider>
                          </v-card-text>
                          <v-btn color='#553D80' @click="dialog=false">Сохранить</v-btn>
                      </v-card>
        </v-dialog>
    <v-spacer/>
    <v-toolbar-items>
      <v-flex
        align-center
        layout
        py-2>
        <router-link
          v-ripple
          class="toolbar-items"
          to="/">
          <v-icon>mdi-home</v-icon>
        </router-link>
        <v-menu
          bottom
          left
          color="white"
          content-class
          offset-y
          transition="slide-y-transition">
          <router-link
            v-ripple
            slot="activator"
            class="toolbar-items"
            to="/"
          >
            <v-badge
              color="error"
              overlap>
              <template slot="badge">{{ notifications.length }}</template>
              <v-icon color>mdi-bell</v-icon>
            </v-badge>
          </router-link>
          <v-card>
            <v-list dense>
                  <v-list-tile
                    v-for="item in notifications"
                    :key="item">
                    <v-list-tile-title>
                      {{ item.rank+ ' '+item.surname+' '+item.name+' '+item.otchestvo+' имеет много нарушений.' }}
                    </v-list-tile-title>
                  </v-list-tile>
                </v-list>
          </v-card>
        </v-menu>
        <v-icon
        class="toolbar-items"
        @click='dialog=true'
        >
          mdi-android-debug-bridge
        </v-icon>
        <v-icon
          class="toolbar-items"
          color
          @click="logout">mdi-power</v-icon>
      </v-flex>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'
import axios from 'axios'
export default {
  data: () => ({
    notifications: {},
    dialog:false,
    title: 'I got a digital dash -Future Hendrixx',
    responsive: false,
    responsiveInput: false,
    value: 2,
      rules: [
        v => v <= 10 || 'Внимание больше 10 полных проверок в день может привести к перегрузке сервиса',
      ],
    value1: 50,
      rules1: [
        v => v <= 60 || 'Внимание больше 50 сканирований в минуту может привести к перегрузке сервиса',
      ],
    value2: 3,
      rules2: [
        v => v <= 5 || 'Использование больше 5 ядер может привести к перегрузке сервиса',
      ],
  }),

  computed: {
    ...mapGetters(['authorized'])
  },

  watch: {
    $route (val) {
      this.title = val.meta.name
    }
  },

  mounted () {
    this.onResponsiveInverted()
    window.addEventListener('resize', this.onResponsiveInverted)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResponsiveInverted)
  },
  created() {
    let headers = {
        'Content-Type': 'application/json',
        'Authorization': 'jwt '.concat(localStorage['token'])
          }
    axios
      .get('http://127.0.0.1:8000/space/notification',{headers})
      .then(response => (this.notifications) = response.data)
  },

  methods: {
    ...mapMutations('app', ['setDrawer', 'toggleDrawer']),
    onClickBtn () {
      this.setDrawer(!this.$store.state.app.drawer)
    },
    onClick () {
      //
    },

    onResponsiveInverted () {
      if (window.innerWidth < 991) {
        this.responsive = true
        this.responsiveInput = false
      } else {
        this.responsive = false
        this.responsiveInput = true
      }
    },
    logout: function () {
      this.$store.dispatch('logout').then(() => {
        this.$router.push('/')
      })
    }
  }
}
</script>

<style>
	#core-toolbar a {
		text-decoration: none;
	}
</style>
