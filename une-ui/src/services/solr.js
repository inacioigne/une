import axios from "axios";

function search() {
    const api = axios.create({
        baseURL: "http://45.178.180.130:8983/solr/search/",
      });
    
      return api;
}

export const api = search();