
import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import { getLastSiteUsages } from '../axios/usersAxios';
import {fillLastUsage} from '../redux/actions/sitesActions'
import ElementorLogo from './Screenshot 2023-07-13 153352.png';

import { useDispatch, useSelector } from 'react-redux';

export const SitePreview  = () => {
  const [usageData, setUsageData] = useState([]);

  let d=useDispatch()


  let currentSiteId=useSelector(x=>x.sitesReducer. currenSiteId)
  console.log(currentSiteId);

  useEffect(() => {
    getLastSiteUsages(currentSiteId, 10).then(x=>{ setUsageData(x.data)})
  }, []);
  const graphStyle = {
   
    
  };

  // Extract the resource data for each resource
  const storageGbData = {
    x: usageData.map(item => item.time),
    y: usageData.map(item => item.storage_gb),
    name: 'Storage GB',
    marker: {
      color: 'red',
    },
  };
  const discCacheData = {
    x: usageData.map(item => item.time),
    y: usageData.map(item => item.disc_cache),
    name: 'Disc Cache',
    marker: {
      color: 'red',
    },
  };
  const discAData = {
    x: usageData.map(item => item.time),
    y: usageData.map(item => item.disc_a_gb),
    name: 'Disc A GB',
    marker: {
      color: 'red',
    },
  };
  const discBData = {
    x: usageData.map(item => item.time),
    y: usageData.map(item => item.disc_b_gb),
    name: 'Disc B GB',
    marker: {
      color: 'red',
    },
  };
  const cpuPercentData = {
    x: usageData.map(item => item.time),
    y: usageData.map(item => item.cpu_percent),
    name: 'CPU Percent',
    marker: {
      color: '#F9A8D4',
    },
  };
  const cpuTicData = {
    x: usageData.map(item => item.time),
    y: usageData.map(item => item.cpu_tic),
    name: 'CPU TIC',
    marker: {
      color: 'red',
    },
  };

  return (
    <div style={{ backgroundColor: 'black', padding: '10px' }}>
      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '20px' }}>
        <img src={ElementorLogo} alt="Elementor Logo" style={{ width: '60px', marginRight: '10px' }} />
        <h2 style={{ color: '#ffffff' }}>Usage for Site {currentSiteId}</h2>
      </div>
      <span style={{ padding: '2px' }}>
        <Plot data={[storageGbData]} layout={{ title: 'Storage GB Usage', plot_bgcolor:'#ffffff' , paper_bgcolor: 'black'}} />
      </span>
      <span style={{ padding: '2px' }}>
        <Plot data={[discCacheData]} layout={{ title: 'Disc Cache Usage' , plot_bgcolor:'#ffffff' , paper_bgcolor: 'black'}}/>
      </span>
      <span style={{ padding: '2px' }}>
        <Plot data={[discAData]} layout={{ title: 'Disc A GB Usage', plot_bgcolor:'#ffffff' , paper_bgcolor: 'black'}}/>
      </span>
      <span style={{ padding: '2px' }}>
        <Plot data={[discBData]} layout={{ title: 'Disc B GB Usage', plot_bgcolor:'#ffffff' , paper_bgcolor: 'black'}} />
      </span>
      <span style={{ padding: '2px' }}>
        <Plot data={[cpuPercentData]} layout={{ title: 'CPU Percent Usage' , plot_bgcolor:'#ffffff' , paper_bgcolor: 'black'}} />
      </span>
      <span style={{ padding: '2px' }}>
        <Plot data={[cpuTicData]} layout={{ title: 'CPU TIC Usage' , plot_bgcolor:'#ffffff' , paper_bgcolor: 'black'}} />
      </span>
    </div>
  );
  
};




