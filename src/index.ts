import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ISettingRegistry } from '@jupyterlab/settingregistry';

import { requestAPI } from './handler';

/**
 * Initialization data for the @educational-technology-collective/etc_jupyter_server_extension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '@educational-technology-collective/etc_jupyter_server_extension:plugin',
  autoStart: true,
  optional: [ISettingRegistry],
  activate: (app: JupyterFrontEnd, settingRegistry: ISettingRegistry | null) => {
    console.log('JupyterLab extension @educational-technology-collective/etc_jupyter_server_extension is activated!');

    requestAPI<any>('version')
    .then(data => {
      console.log('etc_jupyter_server_extension', data);
    })
    .catch(reason => {
      console.error(
        `The etc_jupyter_server_extension server extension appears to be missing.\n${reason}`
      );
    });
  }
};

export default plugin;
