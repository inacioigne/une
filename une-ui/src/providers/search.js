import { createContext, useContext, useState } from "react";
import { api } from "src/services/solr";

export const SearchContext = createContext({});

const facet = {
  institution: {
    field: "institution"
  },
  subject: { 
    field: "marc650a_str",
  },
  author: {
    field: "marc100a_str",
  },
  year: {
    field: "marc260c",
  },
  type: {
    field: "marc990a",
  },
};

export const SearchProvider = ({ children }) => {
  const [numFound, setNumFound] = useState(0);
  const [items, setItems] = useState(null);
  const [facetInstitution, setfacetInstitution] = useState(null);
  const [facetSuject, setfacetSuject] = useState(null);
  const [facetAuthor, setfacetAuthor] = useState(null);
  const [facetYear, setfacetYear] = useState(null);
  const [facetType, setfacetType] = useState(null);
  const [filter, setFilter] = useState([])

    const getData = (field, term,) => {
      //console.log("CTX: ", field, term);

      const json_filter = {
        filter: filter,
      };

    api
      .get("select", {
        params: {
          q: `${field}:${term}`,
        //   start: page,
        //   "q.op": "AND",
           json: JSON.stringify(json_filter),
           facet: true,
           "json.facet": JSON.stringify(facet),
          wt: "json",
        },
      })
      .then((response) => {
        //console.log("CTX: ", response.data);
         setNumFound(response.data.response.numFound);
         setItems(response.data.response.docs);
         setfacetInstitution(response.data.facets.institution.buckets);
         setfacetSuject(response.data.facets.subject.buckets);
         setfacetAuthor(response.data.facets.author.buckets);
         setfacetYear(response.data.facets.year.buckets);
         setfacetType(response.data.facets.type.buckets);
      })
      .catch(function (error) {
        console.log(error);
      });

    }
  return (
    <SearchContext.Provider
      value={{
        getData,
        items,
        facetSuject, facetAuthor, facetYear, facetType, facetInstitution,
        numFound,
        filter, setFilter,
      }}
    >
      {children}
    </SearchContext.Provider>
  );
};

export const useSearch = () => useContext(SearchContext);
