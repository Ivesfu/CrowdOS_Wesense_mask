<template>
  <div class="tables-basic">
    <h2 class="page-title">数据展示</h2>
    <b-row>
      <b-col>
        <Widget
          title="<h5>人群口罩佩戴情况分析</h5>"
          customHeader settings close
        >
          <div class="table-resposive">
            <table class="table">
              <thead>
                <tr>
                  <th class="hidden-sm-down">序号</th>
                  <th>Picture</th>
                  <th>Description</th>
                  <th class="hidden-sm-down">识别的总人数</th>
                  <th class="hidden-sm-down">带口罩的人数</th>
                  <th class="hidden-sm-down">带口罩的比例</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in slist" :key="index">
                  <td>{{ index + 1 }}</td>
                    <img
                      class="img-rounded"
                      :src = "require('../../assets/myicons/' + (index + 1) + '.jpg')" 
                      alt=""
                      height="60"
                    />
                  <td>
                    {{ klist[index] }}
                  </td>
                  <td class="text-semi-muted">
                    {{ item["tot"] }}
                  </td>
                  <td class="text-semi-muted">
                   {{ item["mask"] }}
                  </td>
                  <td class="width-150">
                    {{ item["info"] }}
                  </td>

                </tr>
              </tbody>
            </table>
          </div>
          <div class="clearfix">
            <div class="float-right">
              <b-button variant="default" class="mr-3" size="sm">Send to...</b-button>
              <b-dropdown variant="inverse" class="mr-xs" size="sm" text="Clear" right>
                <b-dropdown-item>Clear</b-dropdown-item>
                <b-dropdown-item>Move ...</b-dropdown-item>
                <b-dropdown-item>Something else here</b-dropdown-item>
                <b-dropdown-divider />
                <b-dropdown-item>Separated link</b-dropdown-item>
              </b-dropdown>
            </div>
            <p>Basic table with styled content</p>
          </div>
        </Widget>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Vue from 'vue';
import Widget from '@/components/Widget/Widget';
import Sparklines from '../../components/Sparklines/Sparklines'

export default {
  name: 'Tables',
  components: { Widget, Sparklines },
  data() {
    return {
      slist:[],
      photolist:[],
      klist:[],
      tableStyles: [
        {
          id: 1,
          picture: require('../../assets/myicons/1.jpg'), // eslint-disable-line global-require
          description: 'Palo Alto',
          info: {
            type: 'JPEG',
            dimensions: '200x150',
          },
          date: new Date('September 14, 2012'),
          size: '45.6 KB',
          progress: {
            percent: 29,
            colorClass: 'success',
          },
        },
        {
          id: 2,
          picture: require('../../assets/myicons/2.jpg'), // eslint-disable-line global-require
          description: 'The Sky',
          info: {
            type: 'PSD',
            dimensions: '2400x1455',
          },
          date: new Date('November 14, 2012'),
          size: '15.3 MB',
          progress: {
            percent: 33,
            colorClass: 'warning',
          },
        },
        {
          id: 3,
          picture: require('../../assets/myicons/3.jpg'), // eslint-disable-line global-require
          description: 'Down the road',
          label: {
            colorClass: 'danger',
            text: 'INFO!',
          },
          info: {
            type: 'JPEG',
            dimensions: '200x150',
          },
          date: new Date('September 14, 2012'),
          size: '49.0 KB',
          progress: {
            percent: 38,
            colorClass: 'inverse',
          },
        },
        {
          id: 4,
          picture: require('../../assets/myicons/4.jpg'), // eslint-disable-line global-require
          description: 'The Edge',
          info: {
            type: 'PNG',
            dimensions: '210x160',
          },
          date: new Date('September 15, 2012'),
          size: '69.1 KB',
          progress: {
            percent: 17,
            colorClass: 'danger',
          },
        },
        {
          id: 5,
          picture: require('../../assets/myicons/5.jpg'), // eslint-disable-line global-require
          description: 'Fortress',
          info: {
            type: 'JPEG',
            dimensions: '1452x1320',
          },
          date: new Date('October 1, 2012'),
          size: '2.3 MB',
          progress: {
            percent: 41,
            colorClass: 'primary',
          },
        },
      ],
    };
  },
  mounted() {
    this.draw1();
  },
  methods: {
    draw1() {
      this.$http
        .get("http://8.130.172.72:8080/api/demo/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
          this.slist = res.data;
          for(var i = 0; i < this.slist.length; ++i){
              var t = "../../assets/myicons/" + i + 1 + ".jpg";
              console.log(t);
              this.photolist.push(t);
           }
        });
        this.klist.push("机场场合");
        this.klist.push("火车站场合");
        this.klist.push("公园社区场合");
        this.klist.push("商场场合");
        this.klist.push("景区场合");
        this.klist.push("学校场合");
        this.klist.push("医院场合");
        this.klist.push("America");
        this.klist.push("国外场景");
        this.klist.push("国外学校场合");
        this.klist.push("国外医院场合");
        this.$forceUpdate();
    },
    parseDate(date) {
      const dateSet = date.toDateString().split(' ');
      return `${date.toLocaleString('en-us', { month: 'long' })} ${dateSet[2]}, ${dateSet[3]}`;
    },
    checkAll(ev, checkbox) {
      const checkboxArr = (new Array(this[checkbox].length)).fill(ev.target.checked);
      Vue.set(this, checkbox, checkboxArr);
    },
    getRandomColor() {
      const {primary, success, info, danger} = this.appConfig.colors;
      const colors = [info, primary, danger, success];
      return {colors: [colors[Math.floor(Math.random() * colors.length)]]}
    }
  },
};
</script>

<style src="./Basic.scss" lang="scss" scoped />
