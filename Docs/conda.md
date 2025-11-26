# Uploading and installing conda packages

Anaconda.org is a centralized package <Tooltip tip="Any storage location from which software or software assets, like packages, can be retrieved and installed on a local computer.">repository</Tooltip> and distribution platform for the conda ecosystem. The site enables you to both upload your own conda packages and discover conda packages created by other users.

<Note>
  To work with conda packages, you must use the corresponding subdomain `https://conda.anaconda.org`. To install conda packages from the user `travis`, for example, use the <Tooltip tip="Any storage location from which software or software assets, like packages, can be retrieved and installed on a local computer.">repository</Tooltip> URL `https://conda.anaconda.org/travis`.
</Note>

## Uploading conda packages

This example shows how to build and upload a [conda](https://docs.conda.io/projects/conda-build/en/stable/index.html) package to Anaconda.org using `conda build`.

1. Open Anaconda Prompt (Terminal on macOS/Linux).

2. If necessary, install the `anaconda-client` and `conda-build` packages by running the following command:

   ```sh  theme={null}
   conda install anaconda-client conda-build
   ```

3. Choose the repository for which you would like to build the package. In this example, we use a small public [conda test package](https://github.com/Anaconda-Platform/anaconda-client/tree/master/example-packages/conda):

   ```sh  theme={null}
   # Replace <PACKAGE> with the package name
   git clone https://github.com/Anaconda-Platform/anaconda-client
   cd anaconda-client/<PACKAGE>/conda/
   ```

   There are two required files in the example package: [meta.yaml](https://github.com/Anaconda-Platform/anaconda-client/blob/master/example-packages/conda/meta.yaml) and [build.sh](https://github.com/Anaconda-Platform/anaconda-client/blob/master/example-packages/conda/build.sh).

   macOS and Linux systems are Unix-like systems. Packages built for Unix-like systems require a `build.sh` file, packages built for Windows require a `bld.bat` file, and packages built for both Windows and Unix-like systems require both a `build.sh` file and a `bld.bat` file. All packages require a `meta.yaml` file.

4. To build the package, turn off automatic Client uploading and then run the `conda build` command:

   ```sh  theme={null}
   conda config --set anaconda_upload no
   conda build .
   ```

   All packages built using the `conda build` command are placed in a subdirectory of the [Anaconda](/getting-started/anaconda/main) `conda-bld` directory.

   <Tip>
     You can check where the resulting file was placed by adding the `--output` option:

     ```sh  theme={null}
     conda build . --output
     ```
   </Tip>

5. Upload the test package to Anaconda.org by running the `anaconda upload` command:

   ```sh  theme={null}
   anaconda login

   # Replace </PATH/TO/PACKAGE_NAME> with the correct file path and package name
   # Packages can be uploaded with .tar.bz2 or .conda compression formats
   anaconda upload </PATH/TO/PACKAGE_NAME>.tar.bz2
   anaconda upload </PATH/TO/PACKAGE_NAME>.conda
   ```

For more information on the `.conda` format, see [Using the .conda compression format](/tools/anaconda-org/user-guide/packages/manage-packages#using-the-conda-compression-format).

For more information on conda's overall build framework, see [Building conda packages](https://docs.conda.io/projects/conda-build/en/stable/concepts/recipe.html) in the official conda docs.

## Installing conda packages

You can install conda packages from Anaconda.org by adding <Tooltip tip="A location (URL or file path) in a repository where conda looks for packages.">channels</Tooltip> to your conda configuration.

### Public channels

1. Open Anaconda Prompt (Terminal on macOS/Linux).

2. Because conda knows how to interact with Anaconda.org, specifying the channel `sean`, for example, translates to [https://anaconda.org/sean](https://anaconda.org/sean):

   ```sh  theme={null}
   conda config --add channels sean
   ```

3. You can now install public conda packages from Sean's Anaconda.org account. Try installing the `testci` package at [https://anaconda.org/sean/testci](https://anaconda.org/sean/testci):

   ```sh  theme={null}
   conda install testci
   ```

### Private channels

You can install a package from a private channel with a <Tooltip tip="A randomly generated string that proves your identity and permission to access resources like channels, packages, or APIs.">token</Tooltip> and a [Label](/tools/anaconda-org/user-guide/work-with-labels):

```sh  theme={null}
# Replace <TOKEN> with the provided token
# Replace <CHANNEL> with a user channel
# Replace <LABEL_NAME> with the label name
# Replace <PACKAGE> with the name of the package you want to install
conda install --channel https://conda.anaconda.org/t/<TOKEN>/<CHANNEL>/label/<LABEL_NAME> <PACKAGE>
```

Tokens are only required if the channel is private.

## Finding help for uploading packages

You can obtain a complete list of upload options, including:

* Package channel
* Label
* Availability to other users
* Metadata

To list the options, run the following in Anaconda Prompt (Terminal on macOS/Linux):

```sh  theme={null}
anaconda upload -h
```

# Uploading and installing conda packages

Anaconda.org is a centralized package <Tooltip tip="Any storage location from which software or software assets, like packages, can be retrieved and installed on a local computer.">repository</Tooltip> and distribution platform for the conda ecosystem. The site enables you to both upload your own conda packages and discover conda packages created by other users.

<Note>
  To work with conda packages, you must use the corresponding subdomain `https://conda.anaconda.org`. To install conda packages from the user `travis`, for example, use the <Tooltip tip="Any storage location from which software or software assets, like packages, can be retrieved and installed on a local computer.">repository</Tooltip> URL `https://conda.anaconda.org/travis`.
</Note>

## Uploading conda packages

This example shows how to build and upload a [conda](https://docs.conda.io/projects/conda-build/en/stable/index.html) package to Anaconda.org using `conda build`.

1. Open Anaconda Prompt (Terminal on macOS/Linux).

2. If necessary, install the `anaconda-client` and `conda-build` packages by running the following command:

   ```sh  theme={null}
   conda install anaconda-client conda-build
   ```

3. Choose the repository for which you would like to build the package. In this example, we use a small public [conda test package](https://github.com/Anaconda-Platform/anaconda-client/tree/master/example-packages/conda):

   ```sh  theme={null}
   # Replace <PACKAGE> with the package name
   git clone https://github.com/Anaconda-Platform/anaconda-client
   cd anaconda-client/<PACKAGE>/conda/
   ```

   There are two required files in the example package: [meta.yaml](https://github.com/Anaconda-Platform/anaconda-client/blob/master/example-packages/conda/meta.yaml) and [build.sh](https://github.com/Anaconda-Platform/anaconda-client/blob/master/example-packages/conda/build.sh).

   macOS and Linux systems are Unix-like systems. Packages built for Unix-like systems require a `build.sh` file, packages built for Windows require a `bld.bat` file, and packages built for both Windows and Unix-like systems require both a `build.sh` file and a `bld.bat` file. All packages require a `meta.yaml` file.

4. To build the package, turn off automatic Client uploading and then run the `conda build` command:

   ```sh  theme={null}
   conda config --set anaconda_upload no
   conda build .
   ```

   All packages built using the `conda build` command are placed in a subdirectory of the [Anaconda](/getting-started/anaconda/main) `conda-bld` directory.

   <Tip>
     You can check where the resulting file was placed by adding the `--output` option:

     ```sh  theme={null}
     conda build . --output
     ```
   </Tip>

5. Upload the test package to Anaconda.org by running the `anaconda upload` command:

   ```sh  theme={null}
   anaconda login

   # Replace </PATH/TO/PACKAGE_NAME> with the correct file path and package name
   # Packages can be uploaded with .tar.bz2 or .conda compression formats
   anaconda upload </PATH/TO/PACKAGE_NAME>.tar.bz2
   anaconda upload </PATH/TO/PACKAGE_NAME>.conda
   ```

For more information on the `.conda` format, see [Using the .conda compression format](/tools/anaconda-org/user-guide/packages/manage-packages#using-the-conda-compression-format).

For more information on conda's overall build framework, see [Building conda packages](https://docs.conda.io/projects/conda-build/en/stable/concepts/recipe.html) in the official conda docs.

## Installing conda packages

You can install conda packages from Anaconda.org by adding <Tooltip tip="A location (URL or file path) in a repository where conda looks for packages.">channels</Tooltip> to your conda configuration.

### Public channels

1. Open Anaconda Prompt (Terminal on macOS/Linux).

2. Because conda knows how to interact with Anaconda.org, specifying the channel `sean`, for example, translates to [https://anaconda.org/sean](https://anaconda.org/sean):

   ```sh  theme={null}
   conda config --add channels sean
   ```

3. You can now install public conda packages from Sean's Anaconda.org account. Try installing the `testci` package at [https://anaconda.org/sean/testci](https://anaconda.org/sean/testci):

   ```sh  theme={null}
   conda install testci
   ```

### Private channels

You can install a package from a private channel with a <Tooltip tip="A randomly generated string that proves your identity and permission to access resources like channels, packages, or APIs.">token</Tooltip> and a [Label](/tools/anaconda-org/user-guide/work-with-labels):

```sh  theme={null}
# Replace <TOKEN> with the provided token
# Replace <CHANNEL> with a user channel
# Replace <LABEL_NAME> with the label name
# Replace <PACKAGE> with the name of the package you want to install
conda install --channel https://conda.anaconda.org/t/<TOKEN>/<CHANNEL>/label/<LABEL_NAME> <PACKAGE>
```

Tokens are only required if the channel is private.

## Finding help for uploading packages

You can obtain a complete list of upload options, including:

* Package channel
* Label
* Availability to other users
* Metadata

To list the options, run the following in Anaconda Prompt (Terminal on macOS/Linux):

```sh  theme={null}
anaconda upload -h
```
# Installation

The following sections detail the process for installing and accessing the Anaconda Toolbox Excel add-in. Once installed, get to know your newly added functionality through our [Anaconda Toolbox](/tools/excel/toolbox/visualize) and [Anaconda Code](/tools/excel/code) documentation.

<Note>
  [Anaconda Code](/tools/excel/code) is included in the Anaconda Toolbox installation.
</Note>

## Installing the Anaconda Toolbox Excel add-in

<Tip>
  Get started with Anaconda Toolbox instantly:

  * [Open in Excel desktop](ms-excel:https://api.addins.store.office.com/addinstemplate/en-US/db952600-d470-4eb4-917d-6b2313fc5a7a/WA200006518/none/AnacondaToolbox.xlsx?omexsrctype=1) — requires Excel to be installed on your computer
  * [Open in Excel online](https://go.microsoft.com/fwlink/?linkid=2261819\&templateid=WA200006518\&templatetitle=AnacondaToolbox)

  Company VPNs or firewall settings may affect these links. If you encounter any issues, follow the steps below.
</Tip>

<Steps>
  <Step title="Visit Microsoft AppSource">
    Go to the [Anaconda Toolbox product page on Microsoft AppSource](https://appsource.microsoft.com/en-us/product/office/WA200006518?src=office\&corrid=e512e195-e06f-1a72-091c-b019258ac57c\&omexanonuid=\&referralurl=\&ClientSessionId=222d10cb-7f3d-400b-a75f-0d51b0ba4ab9).
  </Step>

  <Step title="Get the Add-in">
    Click **Get it now**, then follow the onscreen instructions to open.
  </Step>

  <Step title="Restart Excel">
    If necessary, close and reopen Excel for your changes to take effect.
  </Step>
</Steps>

## Adding the Anaconda Toolbox Excel add-in to your ribbon

<Steps>
  <Step title="Navigate to Add-ins">
    From the **Home** tab, click **Add-ins**, then search for *Anaconda*. You should see the **AnacondaToolbox** add-in.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/IBO7780zo4xe9zAp/images/add_ins.png?fit=max&auto=format&n=IBO7780zo4xe9zAp&q=85&s=c329eea470525b70a3293d1026932921" alt="" data-og-width="1922" width="1922" data-og-height="846" height="846" data-path="images/add_ins.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/IBO7780zo4xe9zAp/images/add_ins.png?w=280&fit=max&auto=format&n=IBO7780zo4xe9zAp&q=85&s=8c21d0b446d249500ac88c0262e21a42 280w, https://mintcdn.com/anaconda-29683c67/IBO7780zo4xe9zAp/images/add_ins.png?w=560&fit=max&auto=format&n=IBO7780zo4xe9zAp&q=85&s=0391cb4c132048d213c3eb12f8988f31 560w, https://mintcdn.com/anaconda-29683c67/IBO7780zo4xe9zAp/images/add_ins.png?w=840&fit=max&auto=format&n=IBO7780zo4xe9zAp&q=85&s=fc759d8506901867b44cf1c5787e1e04 840w, https://mintcdn.com/anaconda-29683c67/IBO7780zo4xe9zAp/images/add_ins.png?w=1100&fit=max&auto=format&n=IBO7780zo4xe9zAp&q=85&s=0d8226d4e68f81efacea8fbcbb84cafb 1100w, https://mintcdn.com/anaconda-29683c67/IBO7780zo4xe9zAp/images/add_ins.png?w=1650&fit=max&auto=format&n=IBO7780zo4xe9zAp&q=85&s=233826a6f1c8144d27363629887f035f 1650w, https://mintcdn.com/anaconda-29683c67/IBO7780zo4xe9zAp/images/add_ins.png?w=2500&fit=max&auto=format&n=IBO7780zo4xe9zAp&q=85&s=d0e3203ebb2a641ec676ab2b63489e98 2500w" />
    </Frame>
  </Step>

  <Step title="Add the Tool">
    Click **Add**.
  </Step>
</Steps>

<Note>
  If **AnacondaToolbox** does not appear, click **More Add-ins** and search again in the dialog that appears.
</Note>

### Launching Anaconda Toolbox

<Steps>
  <Step title="Access the Ribbon">
    After installing the add-in, go to the **Formulas** tab in Excel's Ribbon.
  </Step>

  <Step title="Launch Anaconda Toolbox">
    Select **Anaconda Toolbox** to open the Toolbox panel.
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_toolbox_home.png?fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=e72dfb5d49dfb8383b9e7cf322d3ac86" alt="Anaconda Toolbox interface within Excel showing data visualization and analysis tools" data-og-width="3460" width="3460" data-og-height="2040" height="2040" data-path="images/excel_toolbox_home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_toolbox_home.png?w=280&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=0af34673d12426365ed9b6d7da106c9c 280w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_toolbox_home.png?w=560&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=4ba5995427c6914e3a9527432f390409 560w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_toolbox_home.png?w=840&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=8b1b4db649cf59661aede36227b0ea86 840w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_toolbox_home.png?w=1100&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=a2ae0b84d3529be9f986f4ba93bdad50 1100w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_toolbox_home.png?w=1650&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=1cf1ea349b2d627df7989598be92ceb7 1650w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_toolbox_home.png?w=2500&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=4d49462f5dc5a936ad7e243b1508cfff 2500w" />
</Frame>

### Launching Anaconda Code

<Steps>
  <Step title="Access the Ribbon">
    After installing the add-in, go to the **Formulas** tab in Excel's Ribbon.
  </Step>

  <Step title="Launch Anaconda Code">
    Click **Anaconda Code** to open the Code panel.
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_code_home.png?fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=5dc141f634464f0e405402b91c5803e0" alt="Anaconda Code interface showing Python code editor within Excel" data-og-width="3460" width="3460" data-og-height="2044" height="2044" data-path="images/excel_code_home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_code_home.png?w=280&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=193997042194462aab3cc243a3c7aa3b 280w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_code_home.png?w=560&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=670290b093f622d67a90a01a3f068645 560w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_code_home.png?w=840&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=5fca79c1ef18da8449211ac84b6431e7 840w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_code_home.png?w=1100&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=660ff9e4fa5a3e5638f408980eda73c7 1100w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_code_home.png?w=1650&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=57ad03cb86cb1625aee170661fe89b42 1650w, https://mintcdn.com/anaconda-29683c67/pkzYO2NjYT2e8NeP/images/excel_code_home.png?w=2500&fit=max&auto=format&n=pkzYO2NjYT2e8NeP&q=85&s=95ed36629fae5dafe71a1047dd61b2ba 2500w" />
</Frame>


# Anaconda Code

export const ExcelRefIcon = () => {
  return <span className="inline_icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 60.51 26.3">
            <path fill="currentColor" d="M0,26.3V0H8.89c2.05,0,3.74,.35,5.06,1.05,1.32,.7,2.29,1.65,2.93,2.87,.63,1.22,.95,2.6,.95,4.15s-.32,2.92-.95,4.12c-.63,1.2-1.61,2.14-2.92,2.82-1.31,.68-2.98,1.02-5.02,1.02H1.75v-2.88h7.09c1.4,0,2.54-.21,3.4-.62s1.49-1,1.88-1.75,.58-1.66,.58-2.72-.2-1.97-.59-2.76c-.39-.79-1.02-1.4-1.89-1.83-.87-.43-2.01-.65-3.43-.65H3.19V26.3H0ZM12.38,14.49l6.47,11.82h-3.7l-6.37-11.82h3.6Z" /><path fill="currentColor" d="M23.12,26.3V0h15.87V2.83h-12.69V11.71h11.87v2.83h-11.87v8.94h12.89v2.83H23.12Z" /><path fill="currentColor" d="M44.74,26.3V0h15.77V2.83h-12.59V11.71h11.4v2.83h-11.4v11.76h-3.19Z" />
            </svg>
        </span>;
};

export const ExcelCellAddressIcon = () => {
  return <span className="inline_icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 37.91 29.1">
            <path fill="currentColor" d="M3.69,29.1H0L10.68,0h3.64l10.68,29.1h-3.69L12.62,4.6h-.23L3.69,29.1Zm1.36-11.37h14.89v3.13H5.06v-3.13Z" /><path fill="currentColor" d="M37.91,0V29.1h-3.52V3.69h-.17l-7.1,4.72v-3.58L34.38,0h3.52Z" />
            </svg>
        </span>;
};

<Note>
  This feature is currently in beta.
</Note>

Anaconda Code empowers you to write Python or R code and run it locally, directly within Excel. This gives you flexibility and control over the environment in your workbook, allowing you to add and remove <Tooltip tip="Software files and information about the software, such as its name, version, and description, bundled into a file that can be installed and managed by a package manager.">packages</Tooltip> as needed, all while keeping code and data securely within your workbook. Anaconda Code operates independently of Microsoft's Python in Excel feature.

## Initializing Anaconda Code

<Note>
  Anaconda Code is included in the [Anaconda Toolbox installation](/tools/excel/install).
</Note>

When you first launch Anaconda Code, you'll be asked to [sign in to your Anaconda account](https://auth.anaconda.cloud/ui/login/).

If you haven't created an Anaconda Code cell yet, you'll be asked to create one.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=3cde08bfec3755a6dae5d16a6974e404" alt="" style={{ width: "400px" }} data-og-width="832" width="832" data-og-height="1580" height="1580" data-path="images/excel_code_get_started.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=280&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=c90762e302071acaf51c888d70bc8582 280w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=560&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=7b4100827e665c89abe90a656634b2ee 560w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=840&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=c78e4c5fbb86ef0a6b20bfb0ad13fcd4 840w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=1100&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=5d7c3ec52c5f8af8b1d806f04ad3ba0f 1100w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=1650&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=83fa3152537c73d47503c3021078e46a 1650w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=2500&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=a0fbe8f38a065cba09ad7e813c81bcd1 2500w" />
</Frame>

To get started, choose the [language](#running-code) for your new Anaconda Code cell, set the [default link mode](#cell-linking), select the [default output mode](#cell-output), and then click <Icon icon="plus" iconType="regular" /> **Create Code Cell**.

Once you've selected a location for your new Anaconda Code cell, use the editor to start [writing and running code](#running-code).

## Understanding Anaconda Code

Let's take a look at the different elements within Anaconda Code using the <Icon icon="house-chimney" iconType="light" /> **Home** tab for reference:

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=032b6d2170677e6aa91ed7fae804c461" alt="" style={{ width: "400px" }} data-og-width="1026" width="1026" data-og-height="1308" height="1308" data-path="images/code_anatomy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5127e95c25fb99555d35d1154fc40732 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e5afd4320d05b465ee4843e8487e16d2 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=85c39032e894d956c625231b0c68af64 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9b5e9faa437614dc5fbd202534ffbdd0 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0b718c96c73f621232bd8191937ad0ad 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=b3e67c21c827510dec011e1098ff2955 2500w" />
</Frame>

<Steps>
  <Step title="Home" icon={<Icon icon="house-chimney" iconType="light" />}>
    [Create and run Python or R code](#running-code)
  </Step>

  <Step title="Imports and Definitions" icon={<Icon icon="file-import" iconType="light" />}>
    [Customize the code](#customizing-code-initialization) that affects all code
    in your workbook and view script logs
  </Step>

  <Step title="Environment" icon={<Icon icon="laptop-code" iconType="light" />}>
    [Manage the packages and Pyodide or WebR version](#managing-the-environment) for your
    coding environment
  </Step>

  <Step title="Settings" icon={<Icon icon="gear" iconType="light" />}>
    Modify the [default settings for running code](#modifying-workbook-settings)
  </Step>

  <Step title="Account" icon={<Icon icon="user" iconType="light" />}>
    View profile, subscriptions, sign out, and app details
  </Step>

  <Step title="Help" icon={<Icon icon="circle-question" iconType="light" />}>
    Access bug reporting, documentation, community forums, and privacy policy links
  </Step>

  <Step title="Active Code Cell Reference" icon={<ExcelCellAddressIcon />}>
    The active code cell where your [code will run](#running-code)
  </Step>

  <Step title="Linking" icon={<Icon icon="link-simple-slash" iconType="light" />}>
    Toggle [cell linking](#cell-linking) between <Icon icon="link-simple-slash" iconType="light" /> **isolated** and <Icon icon="link-simple" iconType="light" /> **linked** modes
  </Step>

  <Step title="Cell Output" icon={<Icon icon="hashtag" iconType="light" />}>
    Choose whether to output [cell values](#cell-output) as an <Icon icon="hashtag" iconType="light" /> **Excel value** or an <Icon icon="code" iconType="light" /> **Anaconda Code object**
  </Step>

  <Step title="Language" icon={<Icon icon="python" iconType="brands" />}>
    Select <Icon icon="python" iconType="brands" /> **Python** or <Icon icon="r-project" iconType="brands" /> **R** for the code cell
  </Step>

  <Step title="Delete" icon={<Icon icon="trash-can" iconType="light" />}>
    Delete the code cell
  </Step>

  <Step title="Copy" icon={<Icon icon="copy" iconType="light" />}>
    Copy the contents of the code editor
  </Step>

  <Step title="REF" icon={<ExcelRefIcon />}>
    Create a [reference](#using-the-ref-function) to data in the worksheet.
  </Step>

  <Step title="Run" icon={<Icon icon="play" iconType="light" />}>
    Run the code in the active code cell
  </Step>
</Steps>

## Running code

Create an Anaconda Code cell that can run Python or R code using the following steps:

1. From <Icon icon="house-chimney" iconType="light" /> **Home**, click <Icon icon="plus" iconType="regular" aria-label="plus icon" />, then select a cell where you want to insert your code.

   <Tip>
     If you're already in the code editor, select <Icon icon="chevron-down" iconType="light" /> **more** next to the active code cell reference, then <Icon icon="plus" iconType="regular" /> **Add New** to create a new code cell.
   </Tip>

   <Note>
     Subsequent code cells will be in the same language as the previously created one. To change the language, first create a new code cell, then change the code cell's language selection in the code editor.
   </Note>

2. Set the [cell linking and output options](#modifying-workbook-settings).

3. Select Python or R as the code language for the cell.

   <Note>
     If you change the language for the cell to a language you haven't yet used, you might need to click **Load Environment** to load the new language's environment for the first time.
   </Note>

4. Enter your code in the code editor.

5. *(Optional)* If you want to reference a range of data from your spreadsheet or an [Anaconda Code object](/tools/excel/toolbox/data#downloading-data) in your code, click **REF**, then select the range of cells or Anaconda Code cell.

   <Accordion title="Using the REF function">
     When you use **REF** to select data cells or Anaconda Code cells, Anaconda Code creates a `REF` function in your code that returns a list of lists. The [Imports and Definitions](#customizing-code-initialization) tab includes the following pre-defined functions to help convert the returned list of lists to different data structures.

     <Tabs>
       <Tab title="Python">
         | Function                      | Use case                                                                                 | Notes                                                   |
         | :---------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------ |
         | `to_df(REF(<CELL_RANGE>))`    | Create a [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) | `to_df` assumes your data has headers                   |
         | `to_array(REF(<CELL_RANGE>))` | Create a [NumPy](https://numpy.org/) array                                               | `to_array` assumes all data is of the same type         |
         | `to_list(REF(<CELL_RANGE>))`  | Create a 1D list                                                                         | `to_list` handles wide (1 x *n*) or tall (*n* x 1) data |

         You can change the behavior of `to_df()`, `to_array()`, and `to_list()` from the [Imports and Definitions](#customizing-code-initialization) tab.
       </Tab>

       <Tab title="R">
         | Function             | Use case                                                                   | Notes                                                                                     |
         | :------------------- | :------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
         | `to_dataframe()`     | Convert to data.frame or tidyverse [tibble](https://tibble.tidyverse.org/) | Converts a list of lists to tabular format, using first row as column names, if available |
         | `to_matrix()`        | Convert to matrix                                                          | Converts a list of lists to a matrix structure                                            |
         | `to_colwise_list()`  | Convert to column-wise list of vectors                                     | Transforms row-wise data (list of lists) into column-wise format                          |
         | `is_list_of_lists()` | Check data structure                                                       | Helper function that verifies if input is properly structured as a list of lists          |

         You can change the behavior of `to_dataframe`, `to_matrix()`, `to_colwise_list()`,  and `is_list_of_lists()` from the [Imports and Definitions](#customizing-code-initialization) tab.
       </Tab>
     </Tabs>
   </Accordion>

6. Click **Run**. The cell will display the return value of the last evaluated expression. Your changes are automatically saved whenever you re-run the code.

   <Note>
     If you write code that doesn't have a return value (for example, you define a function but don't call the function) and click **Run**, the cell will display `</>NoneType`.
   </Note>

## Editing code

Do not edit your code in the cell itself; instead, modify and re-run your code directly in Anaconda Code.

<Note>
  An Anaconda.com account is required for users to edit shared code.
</Note>

1. From the <Icon icon="house-chimney" iconType="light" /> **Home** page, click <Icon icon="chevron-down" iconType="light" /> **more** on the code you want to edit.
2. Click <Icon icon="pen" iconType="light" /> **Edit in full view** to open the edit view.
3. Adjust your code, then click **Run**.

## Managing the environment

Anaconda Code hosts a single, self-contained environment, which manages the back-end software packages that enable you to run Python or R code within your Excel workbook. You can manage software packages within this environment to extend your code's processing, visualization, and analytical capabilities, and even select the version of [Pyodide](https://pyodide.org/en/stable/) (the WASM engine used by PyScript) or [WebR](https://docs.r-wasm.org/webr/latest/) (the WASM engine used by WebR) that you want to run.

<Warning>
  You can make changes to your environment at any time; however, like with all software projects, altering the environment changes the way the underlying code is interpreted and can cause unintended complications.
</Warning>

### Choosing a Pyodide or WebR version

The latest version of Pyodide or WebR is used by default for all new spreadsheets. For existing spreadsheets, the Pyodide or WebR versions and packages necessary for your code are pinned to the environment.

You can switch versions using the following steps:

1. From the <Icon icon="laptop-code" iconType="light" /> **Environment** tab, click <Icon icon="pen" iconType="light" /> **Edit**.
2. Select the Pyodide or WebR version.
3. Click **Save Changes**.

<Warning>
  A warning will appear if changing the version might result in conflicts with the installed packages. Click **Confirm Update** to proceed or **Cancel** to revert to the previously selected version.
</Warning>

### Managing software packages

1. From the  <Icon icon="laptop-code" iconType="light" /> **Environment** tab, click <Icon icon="pen" iconType="light" /> **Edit**.
2. To add new packages, click <Icon icon="plus" iconType="regular" /> **Add**.
3. *(Optional for Python)* Click the <Icon icon="caret-down" iconType="solid" /> down arrow to add from either PyPI, the PyScript app, or a direct download link to a Python wheel (`.whl`).
4. Search for the package name, then click <Icon icon="plus" iconType="regular" /> **Add** beside the package you want to add.
5. Once you've added all the packages you want to include, click **Add Packages**.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=348fb9b6773a0d83bb96865b4ffd32e2" alt="" style={{ width: "400px" }} data-og-width="1026" width="1026" data-og-height="1580" height="1580" data-path="images/code_add_package.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=7d789112ed04664f7636b4b321d34755 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=fad0116a58ba6f560634eafdefd884a7 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=13eaddaf0de0fe56e5e52afa35fc5cd9 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e9f680eb0753e65901164ee1c51d8e4a 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=65f287b64bfbca38533dfa17cd05269b 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=f25cdcabd0baafec40f544b70665d701 2500w" />
</Frame>

<Note>
  Packages that contain compiled code might not be compatible with the PyScript or R WASM engine. For more information, visit [PyScript.net](https://pyscript.net/) or [r-wasm.org](https://docs.r-wasm.org/webr/latest/packages.html).
</Note>

To remove a package, click <Icon icon="pen" iconType="light" /> **Edit**, then click <Icon icon="trash-can" iconType="regular" /> **Delete** beside the package you want to remove.

## Customizing code initialization

You can think of Anaconda Code's **Imports and Definitions** as an initialization file for your code or like the first cell in a Jupyter Notebook. All code in this section is available to all cells, whether they are [run isolated or linked](#cell-linking).

<AccordionGroup>
  <Accordion title="Imports">
    To customize your code's imports:

    1. On the <Icon icon="file-import" iconType="light" /> **Imports and Definitions** tab, establish the connections to the packages you need to run your code by adding your import statements beneath the `# Add imports` comment.

       <Note>
         You can only `import` from the packages included in the standard Python or Web R installation and those listed in the **Environment** tab.
       </Note>

    2. Click **Apply**.
  </Accordion>

  <Accordion title="Definitions">
    To customize your code's definitions:

    1. From the <Icon icon="file-import" iconType="light" /> **Imports and Definitions** tab, enter any classes or functions you'd like to define beneath the `# Define` comment.

       <Note>
         Anaconda Code comes with pre-defined functions for both Python and R. See [Using the REF function](#using-the-ref-function) to learn more about using these functions.
       </Note>

    2. Click **Apply**.

    You can now call your definitions in the Anaconda Code editor. To call Python functions directly from a spreadsheet cell, follow the steps in [Creating user-defined functions](#creating-user-defined-functions).
  </Accordion>
</AccordionGroup>

### Creating user-defined functions

User-defined functions (UDFs) allow you to write Python or R functions and call them directly from a spreadsheet cell.

<AccordionGroup>
  <Accordion title="UDFs in Python">
    **Creating and calling a UDF**

    1. From the **Imports and Definitions** tab, decorate a function with `@UDF`, as shown in the following example:

       ```py Python UDF Example theme={null}
       @UDF
       def my_custom_function(x, y):
           return x ** y
       ```

    2. Click **Apply**.

    3. In an open cell, enter `=ANACONDA`. If you added the example above to your definitions list, the option to call `ANACONDA.MY_CUSTOM_FUNCTION`
       appears in the dropdown.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5572b0cd0c91b1ec16f37833f8da0072" alt="" data-og-width="1704" width="1704" data-og-height="1428" height="1428" data-path="images/create_udf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=247d5352f34acb749de8c9f02c18240f 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=88f9b79bded922be591f1f8c0ab8ba03 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=066833229713b5d3a64cc6e8037c456c 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=fa27c4109d98adf81c92b28f554e5f86 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9b6d9cd3ee1b3d56255efe1bddc9a93e 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=74d66126646824dc6fc053a42fb8d0fe 2500w" />
       </Frame>

    4. Arrow down to `ANACONDA.MY_CUSTOM_FUNCTION`, press Tab, and then complete the function.

    5. Use Ctrl+Enter (Windows)/Ctrl+Return (macOS) to run the code.

    <Tip>
      If you'd prefer the UDF uses a name other than the function name, use the `name` argument to provide a unique name. Set `nested` to False to remove `ANACONDA.` from the name.

      ```py Renaming Python UDF Example theme={null}
      @UDF(name="MYBANK.PORTFOLIO_ANALYSIS", nested=False)
      def my_custom_function(x, y):
          return x ** y

      ```

      <Frame>
        <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=373fe4433136ca79c235ad8ca82c2f75" alt="" data-og-width="1698" width="1698" data-og-height="1428" height="1428" data-path="images/create_udf_custom_name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0c732829a891824eef2bcd3f1765180d 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=851c16b280782e58675068d8a9f342da 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=7d19999c27fc6440d58bebe0beb2e9f6 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=b69b4fbbc3433f8bc6d85748128a4d7d 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1fcda28ebc077cb9b82a3cc61e397369 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=701b6b1bb35d0ed9a4458461534c76e4 2500w" />
      </Frame>
    </Tip>

    **Using range arguments**

    Specifying a `UDF.Range` argument tells Excel that the input of the function is a 2D range. Without specifying this, Excel will show a `#CALC! Unliftable Array` error if a 2D range is passed into the UDF. Parameters specified as `UDF.Range` will always be passed as a 2D array to the function, even if a single cell is passed in.

    Example usage of `UDF.Range`:

    ```py Python Range Example theme={null}
    @UDF
    def square_me(data: UDF.Range) -> UDF.Range:
        return [[val ** 2 for val in row] for row in data]

    ```

    You can also add type hints for ranges. For example,`UDF.Range[str]`.
  </Accordion>

  <Accordion title="UDFs in R">
    **Creating and calling a UDF**

    1. From the **Imports and Definitions** tab, register the UDF with `UDF.register()` and pass the function as an argument, as shown in the following example:

       <Note>
         The UDF must be registered after the function is defined.
       </Note>

       ```r R UDF Example theme={null}
       my_custom_r_function <- function(x, y) {
           x ^ y
       }
       UDF.register(my_custom_r_function)
       ```

    2. Click **Save and Apply**.

    3. In an open cell, enter `=ANACONDA`. If you added the example above to your definitions list, the option to call `ANACONDA.MY_CUSTOM_R_FUNCTION`
       appears in the dropdown.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=010bdb18a5ff8d5bc2bc38940eb0e120" alt="" data-og-width="1734" width="1734" data-og-height="1716" height="1716" data-path="images/create_udf_r.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1239e88fdc6a9cfa062897f742b8bc1c 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=ffb973876271c5c2f50b60b61b7bb4c2 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=332b09f3ae0ff6e2942ea545ef03ca2a 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0348520653693a4a1ca82e8f6b4ebc29 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=74a2709a286a9b5afadd15175432749d 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=fa64c6ee67a4c6f4e081990aa68b4ad1 2500w" />
       </Frame>

    4. Arrow down to `ANACONDA.MY_CUSTOM_R_FUNCTION`, press Tab, and then complete the function call.

    5. Use Ctrl+Enter (Windows)/Ctrl+Return (macOS) to run the code.

    <Tip>
      If you'd prefer the UDF uses a name other than the function name, register the function with the UDF, then use the `name` argument to provide a unique name and set `nested` to False to remove `ANACONDA.` from the name.

      ```r Renaming R UDF Example theme={null}
      my_custom_r_function <- function(x, y) {
          x ^ y
      }
      UDF.register(my_custom_r_function, name="MYBANK.PORTFOLIO_ANALYSIS", nested=FALSE)
      ```

      <Frame>
        <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=bbe57a6e5a269a3291421899cbbb5654" alt="" data-og-width="1694" width="1694" data-og-height="1712" height="1712" data-path="images/create_udf_r_custom_name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1c8cb2c1c1ad3a50d61d5bbddff9e482 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=69b44583db7858fb51aef174c9687e2d 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e64878144f327129b4cfb363cf60f712 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5a7203d44ecffc992850bdce56bd0fb0 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=13195fc72350cd26e725307f3a8e8ff7 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=2848fabfdc2a327fbe4a6262354cc776 2500w" />
      </Frame>
    </Tip>

    **Using range arguments**

    Setting the `range_args` parameter tells Excel that the input of the function is a 2D range.  Without specifying this, Excel will show a `#CALC! Unliftable Array` error if a 2D range is passed into the UDF. Parameters specified as `range_args` will always be passed as a 2D array to the function, even if a single cell is passed in.

    Example usage of `range_args`:

    ```r R Range Example theme={null}
    my_custom_r_function <- function(data) {
        sum(data)
    }
    UDF.register(my_custom_r_function, range_args=c("data"))
    ```

    **Adding function documentation**

    To add documentation to your function, use the `doc` parameter:

    ```r R Documentation Example theme={null}
    my_custom_r_function <- function(x, y) {
        x ^ y
    }
    UDF.register(my_custom_r_function, doc="Computes x raised to the power of y.")
    ```
  </Accordion>
</AccordionGroup>

## Modifying workbook settings

While you can adjust the settings for running code in your workbook on a case-by-case basis when creating and editing code, you can also assign default settings from the **Settings** tab.

### Cell linking

<AccordionGroup>
  <Accordion title="Run Isolated">
    When a code cell is run in <Icon icon="link-simple-slash" iconType="light" /> **isolated** mode, its code runs independently of other cells. Variables defined within an isolated code cell can't be referenced by other code cells, and variables in other code cells likewise can't be referenced by the isolated code cell.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e28a4ac7b0c21c11b11f4947f303d02c" alt="Two code cells in isolated mode where the second cell cannot access variables from the first" data-og-width="1684" width="1684" data-og-height="948" height="948" data-path="images/cell_isolated_mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=cc926655d310e577b8d716461bab68a6 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=7d8061a23efbb3d233fde9e387c98420 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=bf8d89742812a7cbca0caeca37f2562b 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=2b3785789f9b826b69fe4b6e32e3a76a 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=b552bbb1e33607ce2b90415a01e889ee 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=75b04f2cbcbd411a62405774e632172d 2500w" />
    </Frame>

    In the above image, the `output_of_B2` variable is defined in cell B2 and assigned the string `"I'm the B2 cell!"`. When this code is run in the B2 code cell, the B2 cell displays `"I'm the B2 cell!"`. However, since both cells are running in isolated mode, when `output_of_B2` is referenced in the B4 code cell, the B4 cell displays a `#VALUE!` error because B4 cannot access the variable in B2.

    **Using the `REF` function**

    You can bypass isolation rules as needed using the `REF` function to create a reference from one isolated code cell to another.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=0a6287dd90c0c73498e23d6557133461" alt="A code cell using the REF function to reference another cell's output" data-og-width="1704" width="1704" data-og-height="962" height="962" data-path="images/isolated_ref_cell.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=280&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=b56a71f44090f7a49c6cd2fa07fed96b 280w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=560&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=966d9ab29e616226cd6c3eeca069b4d9 560w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=840&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=78a913f30c04c90f1e3c5f2653d60824 840w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=1100&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=68fed1efc9937f1bbe78c4c4dd9b25c6 1100w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=1650&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=73d17eaa5428cff9c8aa85b61a8f937b 1650w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=2500&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=21f7f82c541d536e9dd555243fd1ed02 2500w" />
    </Frame>

    In the above image, the B4 cell now includes a reference to the B2 cell, `REF("B2")`. When the B4 code cell is run, it returns the value of B2, `"I'm the B2 cell!"`. Changes to the B4 cell don't cause the B2 cell to recalculate, but changes to the B2 cell will cause the B4 cell to recalculate. Code cells can include multiple `REF` function references, and changes to any referenced cells (in this example, B2) will cause the referencing cells to recalculate (in this example, B4).

    **Working with code objects**

    If you reference a cell that's set to output a code object, the `REF` function will return an instance of that object in the referencing cell.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=a88c0a285d085c14ab3c12afe5120cb8" alt="A code cell referencing another cell that outputs a list object" data-og-width="1718" width="1718" data-og-height="968" height="968" data-path="images/code_object_isolated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9701200f23ffc2a1393da4012ea21c45 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=33680dd70b91eb2c9cbe4fddbd252bf7 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e99f2aff1f205424347212780948291c 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=ad5325ba43d4a75b05fbe424db54083c 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=addd1a2ae6323b3829d2ced2df6235dc 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=4d31cd9b92a61ba53043b2ad2e460514 2500w" />
    </Frame>

    In the above image, the B2 code cell is set to output a code object (in this case, a list). Because the output of B2 is a <Tooltip tip="A non-scalar value is a data structure that contains multiple values, such as a list, dictionary, or tuple.">non-scalar value</Tooltip>, we see `</> list` in B2. In the B4 code cell, we define a variable called `output_of_B2` and assign a `REF` function that references cell B2. The output mode for the B4 code cell is set to "Excel Values", so the list spills across multiple cells in the spreadsheet.

    **Benefits of isolated mode**

    The benefit of using the isolated mode is that referenced cells are not recalculated when changes are made to referencing cells. For complex processes, this allows you to:

    * separate code that doesn't change frequently from code you modify often.
    * reduce unnecessary recalculations of computationally intensive operations.
    * create a more modular approach to your data analysis.
    * improve performance when working with larger datasets.
  </Accordion>

  <Accordion title="Run Linked">
    When a code cell is run in <Icon icon="link-simple" iconType="light" /> **linked** mode, variables defined within it can be accessed by any other code cell also running in linked mode. When any linked mode cell is recalculated, all linked mode cells are recalculated. Linked cells run left-to-right, top-to-bottom, and can access objects defined in previously linked cells.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e4be8b9c4344868b197fef9062b442b6" alt="" data-og-width="1698" width="1698" data-og-height="952" height="952" data-path="images/cell_linked_mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=3d8e440d25369edf953f0400a37991c8 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e52b875cdd5cabe82921e39e94cdb9bf 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=4c5f84e2322fb3ea57ef0a60e76c0053 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=be2fc5900b83edc477e12dd6c17c6c1b 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=785ebaa8887db14cc357ee7716cc60be 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=29443653e2dcf1186f59fbccf9a50790 2500w" />
    </Frame>

    In the above image, both the B2 and B4 cell are running in linked mode. The `output_of_B2` variable is defined in cell B2 and assigned the string `"I'm the B2 cell!"`. When this code is run in the B2 code cell, the B2 cell displays `"I'm the B2 cell!"`. The `output_of_B2` variable is then referenced in the B4 code cell, causing the B4 cell to also display `"I'm the B2 cell!"`.

    **Benefits of linked mode**

    Linked mode is useful when:

    * you want to create a continuous workflow across multiple cells.
    * you need to share variables and objects between different parts of your analysis.
    * your code follows a linear execution path.
  </Accordion>
</AccordionGroup>

### Cell output

| Output            | Description                                                                                                                                                                                        |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Excel Values      | When outputting a DataFrame, array, list, and so on, the values will "spill" to fill the required space. If the spill were to overwrite cells containing data, the cell displays a `#SPILL` error. |
| Local Code Object | For certain object types, you can view the contents in a "Card View" by clicking the cell. You can reference this cell and the returned object like you would any other object.                    |

## Troubleshooting

If you encounter an issue that is not listed here, you can obtain support for Anaconda through the [Anaconda community forums](https://forum.anaconda.com) or by [opening a support ticket](https://support.anaconda.com/hc/en-us/requests/new?ticket_form_id=360000993773).

### Error installing functions

<AccordionGroup>
  <Accordion title="Cause">
    This error can occur when Excel loads the Anaconda Toolbox add-in and registers its custom functions. This error happens within Excel and cannot be resolved by the Anaconda Toolbox.
  </Accordion>

  <Accordion title="Solution">
    Close and reopen Excel. If the issue persists, uninstall the Anaconda Toolbox add-in, then reinstall.
  </Accordion>
</AccordionGroup>

# Anaconda Code

export const ExcelRefIcon = () => {
  return <span className="inline_icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 60.51 26.3">
            <path fill="currentColor" d="M0,26.3V0H8.89c2.05,0,3.74,.35,5.06,1.05,1.32,.7,2.29,1.65,2.93,2.87,.63,1.22,.95,2.6,.95,4.15s-.32,2.92-.95,4.12c-.63,1.2-1.61,2.14-2.92,2.82-1.31,.68-2.98,1.02-5.02,1.02H1.75v-2.88h7.09c1.4,0,2.54-.21,3.4-.62s1.49-1,1.88-1.75,.58-1.66,.58-2.72-.2-1.97-.59-2.76c-.39-.79-1.02-1.4-1.89-1.83-.87-.43-2.01-.65-3.43-.65H3.19V26.3H0ZM12.38,14.49l6.47,11.82h-3.7l-6.37-11.82h3.6Z" /><path fill="currentColor" d="M23.12,26.3V0h15.87V2.83h-12.69V11.71h11.87v2.83h-11.87v8.94h12.89v2.83H23.12Z" /><path fill="currentColor" d="M44.74,26.3V0h15.77V2.83h-12.59V11.71h11.4v2.83h-11.4v11.76h-3.19Z" />
            </svg>
        </span>;
};

export const ExcelCellAddressIcon = () => {
  return <span className="inline_icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 37.91 29.1">
            <path fill="currentColor" d="M3.69,29.1H0L10.68,0h3.64l10.68,29.1h-3.69L12.62,4.6h-.23L3.69,29.1Zm1.36-11.37h14.89v3.13H5.06v-3.13Z" /><path fill="currentColor" d="M37.91,0V29.1h-3.52V3.69h-.17l-7.1,4.72v-3.58L34.38,0h3.52Z" />
            </svg>
        </span>;
};

<Note>
  This feature is currently in beta.
</Note>

Anaconda Code empowers you to write Python or R code and run it locally, directly within Excel. This gives you flexibility and control over the environment in your workbook, allowing you to add and remove <Tooltip tip="Software files and information about the software, such as its name, version, and description, bundled into a file that can be installed and managed by a package manager.">packages</Tooltip> as needed, all while keeping code and data securely within your workbook. Anaconda Code operates independently of Microsoft's Python in Excel feature.

## Initializing Anaconda Code

<Note>
  Anaconda Code is included in the [Anaconda Toolbox installation](/tools/excel/install).
</Note>

When you first launch Anaconda Code, you'll be asked to [sign in to your Anaconda account](https://auth.anaconda.cloud/ui/login/).

If you haven't created an Anaconda Code cell yet, you'll be asked to create one.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=3cde08bfec3755a6dae5d16a6974e404" alt="" style={{ width: "400px" }} data-og-width="832" width="832" data-og-height="1580" height="1580" data-path="images/excel_code_get_started.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=280&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=c90762e302071acaf51c888d70bc8582 280w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=560&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=7b4100827e665c89abe90a656634b2ee 560w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=840&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=c78e4c5fbb86ef0a6b20bfb0ad13fcd4 840w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=1100&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=5d7c3ec52c5f8af8b1d806f04ad3ba0f 1100w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=1650&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=83fa3152537c73d47503c3021078e46a 1650w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/excel_code_get_started.png?w=2500&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=a0fbe8f38a065cba09ad7e813c81bcd1 2500w" />
</Frame>

To get started, choose the [language](#running-code) for your new Anaconda Code cell, set the [default link mode](#cell-linking), select the [default output mode](#cell-output), and then click <Icon icon="plus" iconType="regular" /> **Create Code Cell**.

Once you've selected a location for your new Anaconda Code cell, use the editor to start [writing and running code](#running-code).

## Understanding Anaconda Code

Let's take a look at the different elements within Anaconda Code using the <Icon icon="house-chimney" iconType="light" /> **Home** tab for reference:

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=032b6d2170677e6aa91ed7fae804c461" alt="" style={{ width: "400px" }} data-og-width="1026" width="1026" data-og-height="1308" height="1308" data-path="images/code_anatomy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5127e95c25fb99555d35d1154fc40732 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e5afd4320d05b465ee4843e8487e16d2 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=85c39032e894d956c625231b0c68af64 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9b5e9faa437614dc5fbd202534ffbdd0 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0b718c96c73f621232bd8191937ad0ad 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_anatomy.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=b3e67c21c827510dec011e1098ff2955 2500w" />
</Frame>

<Steps>
  <Step title="Home" icon={<Icon icon="house-chimney" iconType="light" />}>
    [Create and run Python or R code](#running-code)
  </Step>

  <Step title="Imports and Definitions" icon={<Icon icon="file-import" iconType="light" />}>
    [Customize the code](#customizing-code-initialization) that affects all code
    in your workbook and view script logs
  </Step>

  <Step title="Environment" icon={<Icon icon="laptop-code" iconType="light" />}>
    [Manage the packages and Pyodide or WebR version](#managing-the-environment) for your
    coding environment
  </Step>

  <Step title="Settings" icon={<Icon icon="gear" iconType="light" />}>
    Modify the [default settings for running code](#modifying-workbook-settings)
  </Step>

  <Step title="Account" icon={<Icon icon="user" iconType="light" />}>
    View profile, subscriptions, sign out, and app details
  </Step>

  <Step title="Help" icon={<Icon icon="circle-question" iconType="light" />}>
    Access bug reporting, documentation, community forums, and privacy policy links
  </Step>

  <Step title="Active Code Cell Reference" icon={<ExcelCellAddressIcon />}>
    The active code cell where your [code will run](#running-code)
  </Step>

  <Step title="Linking" icon={<Icon icon="link-simple-slash" iconType="light" />}>
    Toggle [cell linking](#cell-linking) between <Icon icon="link-simple-slash" iconType="light" /> **isolated** and <Icon icon="link-simple" iconType="light" /> **linked** modes
  </Step>

  <Step title="Cell Output" icon={<Icon icon="hashtag" iconType="light" />}>
    Choose whether to output [cell values](#cell-output) as an <Icon icon="hashtag" iconType="light" /> **Excel value** or an <Icon icon="code" iconType="light" /> **Anaconda Code object**
  </Step>

  <Step title="Language" icon={<Icon icon="python" iconType="brands" />}>
    Select <Icon icon="python" iconType="brands" /> **Python** or <Icon icon="r-project" iconType="brands" /> **R** for the code cell
  </Step>

  <Step title="Delete" icon={<Icon icon="trash-can" iconType="light" />}>
    Delete the code cell
  </Step>

  <Step title="Copy" icon={<Icon icon="copy" iconType="light" />}>
    Copy the contents of the code editor
  </Step>

  <Step title="REF" icon={<ExcelRefIcon />}>
    Create a [reference](#using-the-ref-function) to data in the worksheet.
  </Step>

  <Step title="Run" icon={<Icon icon="play" iconType="light" />}>
    Run the code in the active code cell
  </Step>
</Steps>

## Running code

Create an Anaconda Code cell that can run Python or R code using the following steps:

1. From <Icon icon="house-chimney" iconType="light" /> **Home**, click <Icon icon="plus" iconType="regular" aria-label="plus icon" />, then select a cell where you want to insert your code.

   <Tip>
     If you're already in the code editor, select <Icon icon="chevron-down" iconType="light" /> **more** next to the active code cell reference, then <Icon icon="plus" iconType="regular" /> **Add New** to create a new code cell.
   </Tip>

   <Note>
     Subsequent code cells will be in the same language as the previously created one. To change the language, first create a new code cell, then change the code cell's language selection in the code editor.
   </Note>

2. Set the [cell linking and output options](#modifying-workbook-settings).

3. Select Python or R as the code language for the cell.

   <Note>
     If you change the language for the cell to a language you haven't yet used, you might need to click **Load Environment** to load the new language's environment for the first time.
   </Note>

4. Enter your code in the code editor.

5. *(Optional)* If you want to reference a range of data from your spreadsheet or an [Anaconda Code object](/tools/excel/toolbox/data#downloading-data) in your code, click **REF**, then select the range of cells or Anaconda Code cell.

   <Accordion title="Using the REF function">
     When you use **REF** to select data cells or Anaconda Code cells, Anaconda Code creates a `REF` function in your code that returns a list of lists. The [Imports and Definitions](#customizing-code-initialization) tab includes the following pre-defined functions to help convert the returned list of lists to different data structures.

     <Tabs>
       <Tab title="Python">
         | Function                      | Use case                                                                                 | Notes                                                   |
         | :---------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------ |
         | `to_df(REF(<CELL_RANGE>))`    | Create a [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) | `to_df` assumes your data has headers                   |
         | `to_array(REF(<CELL_RANGE>))` | Create a [NumPy](https://numpy.org/) array                                               | `to_array` assumes all data is of the same type         |
         | `to_list(REF(<CELL_RANGE>))`  | Create a 1D list                                                                         | `to_list` handles wide (1 x *n*) or tall (*n* x 1) data |

         You can change the behavior of `to_df()`, `to_array()`, and `to_list()` from the [Imports and Definitions](#customizing-code-initialization) tab.
       </Tab>

       <Tab title="R">
         | Function             | Use case                                                                   | Notes                                                                                     |
         | :------------------- | :------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
         | `to_dataframe()`     | Convert to data.frame or tidyverse [tibble](https://tibble.tidyverse.org/) | Converts a list of lists to tabular format, using first row as column names, if available |
         | `to_matrix()`        | Convert to matrix                                                          | Converts a list of lists to a matrix structure                                            |
         | `to_colwise_list()`  | Convert to column-wise list of vectors                                     | Transforms row-wise data (list of lists) into column-wise format                          |
         | `is_list_of_lists()` | Check data structure                                                       | Helper function that verifies if input is properly structured as a list of lists          |

         You can change the behavior of `to_dataframe`, `to_matrix()`, `to_colwise_list()`,  and `is_list_of_lists()` from the [Imports and Definitions](#customizing-code-initialization) tab.
       </Tab>
     </Tabs>
   </Accordion>

6. Click **Run**. The cell will display the return value of the last evaluated expression. Your changes are automatically saved whenever you re-run the code.

   <Note>
     If you write code that doesn't have a return value (for example, you define a function but don't call the function) and click **Run**, the cell will display `</>NoneType`.
   </Note>

## Editing code

Do not edit your code in the cell itself; instead, modify and re-run your code directly in Anaconda Code.

<Note>
  An Anaconda.com account is required for users to edit shared code.
</Note>

1. From the <Icon icon="house-chimney" iconType="light" /> **Home** page, click <Icon icon="chevron-down" iconType="light" /> **more** on the code you want to edit.
2. Click <Icon icon="pen" iconType="light" /> **Edit in full view** to open the edit view.
3. Adjust your code, then click **Run**.

## Managing the environment

Anaconda Code hosts a single, self-contained environment, which manages the back-end software packages that enable you to run Python or R code within your Excel workbook. You can manage software packages within this environment to extend your code's processing, visualization, and analytical capabilities, and even select the version of [Pyodide](https://pyodide.org/en/stable/) (the WASM engine used by PyScript) or [WebR](https://docs.r-wasm.org/webr/latest/) (the WASM engine used by WebR) that you want to run.

<Warning>
  You can make changes to your environment at any time; however, like with all software projects, altering the environment changes the way the underlying code is interpreted and can cause unintended complications.
</Warning>

### Choosing a Pyodide or WebR version

The latest version of Pyodide or WebR is used by default for all new spreadsheets. For existing spreadsheets, the Pyodide or WebR versions and packages necessary for your code are pinned to the environment.

You can switch versions using the following steps:

1. From the <Icon icon="laptop-code" iconType="light" /> **Environment** tab, click <Icon icon="pen" iconType="light" /> **Edit**.
2. Select the Pyodide or WebR version.
3. Click **Save Changes**.

<Warning>
  A warning will appear if changing the version might result in conflicts with the installed packages. Click **Confirm Update** to proceed or **Cancel** to revert to the previously selected version.
</Warning>

### Managing software packages

1. From the  <Icon icon="laptop-code" iconType="light" /> **Environment** tab, click <Icon icon="pen" iconType="light" /> **Edit**.
2. To add new packages, click <Icon icon="plus" iconType="regular" /> **Add**.
3. *(Optional for Python)* Click the <Icon icon="caret-down" iconType="solid" /> down arrow to add from either PyPI, the PyScript app, or a direct download link to a Python wheel (`.whl`).
4. Search for the package name, then click <Icon icon="plus" iconType="regular" /> **Add** beside the package you want to add.
5. Once you've added all the packages you want to include, click **Add Packages**.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=348fb9b6773a0d83bb96865b4ffd32e2" alt="" style={{ width: "400px" }} data-og-width="1026" width="1026" data-og-height="1580" height="1580" data-path="images/code_add_package.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=7d789112ed04664f7636b4b321d34755 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=fad0116a58ba6f560634eafdefd884a7 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=13eaddaf0de0fe56e5e52afa35fc5cd9 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e9f680eb0753e65901164ee1c51d8e4a 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=65f287b64bfbca38533dfa17cd05269b 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/code_add_package.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=f25cdcabd0baafec40f544b70665d701 2500w" />
</Frame>

<Note>
  Packages that contain compiled code might not be compatible with the PyScript or R WASM engine. For more information, visit [PyScript.net](https://pyscript.net/) or [r-wasm.org](https://docs.r-wasm.org/webr/latest/packages.html).
</Note>

To remove a package, click <Icon icon="pen" iconType="light" /> **Edit**, then click <Icon icon="trash-can" iconType="regular" /> **Delete** beside the package you want to remove.

## Customizing code initialization

You can think of Anaconda Code's **Imports and Definitions** as an initialization file for your code or like the first cell in a Jupyter Notebook. All code in this section is available to all cells, whether they are [run isolated or linked](#cell-linking).

<AccordionGroup>
  <Accordion title="Imports">
    To customize your code's imports:

    1. On the <Icon icon="file-import" iconType="light" /> **Imports and Definitions** tab, establish the connections to the packages you need to run your code by adding your import statements beneath the `# Add imports` comment.

       <Note>
         You can only `import` from the packages included in the standard Python or Web R installation and those listed in the **Environment** tab.
       </Note>

    2. Click **Apply**.
  </Accordion>

  <Accordion title="Definitions">
    To customize your code's definitions:

    1. From the <Icon icon="file-import" iconType="light" /> **Imports and Definitions** tab, enter any classes or functions you'd like to define beneath the `# Define` comment.

       <Note>
         Anaconda Code comes with pre-defined functions for both Python and R. See [Using the REF function](#using-the-ref-function) to learn more about using these functions.
       </Note>

    2. Click **Apply**.

    You can now call your definitions in the Anaconda Code editor. To call Python functions directly from a spreadsheet cell, follow the steps in [Creating user-defined functions](#creating-user-defined-functions).
  </Accordion>
</AccordionGroup>

### Creating user-defined functions

User-defined functions (UDFs) allow you to write Python or R functions and call them directly from a spreadsheet cell.

<AccordionGroup>
  <Accordion title="UDFs in Python">
    **Creating and calling a UDF**

    1. From the **Imports and Definitions** tab, decorate a function with `@UDF`, as shown in the following example:

       ```py Python UDF Example theme={null}
       @UDF
       def my_custom_function(x, y):
           return x ** y
       ```

    2. Click **Apply**.

    3. In an open cell, enter `=ANACONDA`. If you added the example above to your definitions list, the option to call `ANACONDA.MY_CUSTOM_FUNCTION`
       appears in the dropdown.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5572b0cd0c91b1ec16f37833f8da0072" alt="" data-og-width="1704" width="1704" data-og-height="1428" height="1428" data-path="images/create_udf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=247d5352f34acb749de8c9f02c18240f 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=88f9b79bded922be591f1f8c0ab8ba03 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=066833229713b5d3a64cc6e8037c456c 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=fa27c4109d98adf81c92b28f554e5f86 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9b6d9cd3ee1b3d56255efe1bddc9a93e 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=74d66126646824dc6fc053a42fb8d0fe 2500w" />
       </Frame>

    4. Arrow down to `ANACONDA.MY_CUSTOM_FUNCTION`, press Tab, and then complete the function.

    5. Use Ctrl+Enter (Windows)/Ctrl+Return (macOS) to run the code.

    <Tip>
      If you'd prefer the UDF uses a name other than the function name, use the `name` argument to provide a unique name. Set `nested` to False to remove `ANACONDA.` from the name.

      ```py Renaming Python UDF Example theme={null}
      @UDF(name="MYBANK.PORTFOLIO_ANALYSIS", nested=False)
      def my_custom_function(x, y):
          return x ** y

      ```

      <Frame>
        <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=373fe4433136ca79c235ad8ca82c2f75" alt="" data-og-width="1698" width="1698" data-og-height="1428" height="1428" data-path="images/create_udf_custom_name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0c732829a891824eef2bcd3f1765180d 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=851c16b280782e58675068d8a9f342da 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=7d19999c27fc6440d58bebe0beb2e9f6 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=b69b4fbbc3433f8bc6d85748128a4d7d 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1fcda28ebc077cb9b82a3cc61e397369 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_custom_name.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=701b6b1bb35d0ed9a4458461534c76e4 2500w" />
      </Frame>
    </Tip>

    **Using range arguments**

    Specifying a `UDF.Range` argument tells Excel that the input of the function is a 2D range. Without specifying this, Excel will show a `#CALC! Unliftable Array` error if a 2D range is passed into the UDF. Parameters specified as `UDF.Range` will always be passed as a 2D array to the function, even if a single cell is passed in.

    Example usage of `UDF.Range`:

    ```py Python Range Example theme={null}
    @UDF
    def square_me(data: UDF.Range) -> UDF.Range:
        return [[val ** 2 for val in row] for row in data]

    ```

    You can also add type hints for ranges. For example,`UDF.Range[str]`.
  </Accordion>

  <Accordion title="UDFs in R">
    **Creating and calling a UDF**

    1. From the **Imports and Definitions** tab, register the UDF with `UDF.register()` and pass the function as an argument, as shown in the following example:

       <Note>
         The UDF must be registered after the function is defined.
       </Note>

       ```r R UDF Example theme={null}
       my_custom_r_function <- function(x, y) {
           x ^ y
       }
       UDF.register(my_custom_r_function)
       ```

    2. Click **Save and Apply**.

    3. In an open cell, enter `=ANACONDA`. If you added the example above to your definitions list, the option to call `ANACONDA.MY_CUSTOM_R_FUNCTION`
       appears in the dropdown.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=010bdb18a5ff8d5bc2bc38940eb0e120" alt="" data-og-width="1734" width="1734" data-og-height="1716" height="1716" data-path="images/create_udf_r.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1239e88fdc6a9cfa062897f742b8bc1c 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=ffb973876271c5c2f50b60b61b7bb4c2 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=332b09f3ae0ff6e2942ea545ef03ca2a 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=0348520653693a4a1ca82e8f6b4ebc29 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=74a2709a286a9b5afadd15175432749d 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=fa64c6ee67a4c6f4e081990aa68b4ad1 2500w" />
       </Frame>

    4. Arrow down to `ANACONDA.MY_CUSTOM_R_FUNCTION`, press Tab, and then complete the function call.

    5. Use Ctrl+Enter (Windows)/Ctrl+Return (macOS) to run the code.

    <Tip>
      If you'd prefer the UDF uses a name other than the function name, register the function with the UDF, then use the `name` argument to provide a unique name and set `nested` to False to remove `ANACONDA.` from the name.

      ```r Renaming R UDF Example theme={null}
      my_custom_r_function <- function(x, y) {
          x ^ y
      }
      UDF.register(my_custom_r_function, name="MYBANK.PORTFOLIO_ANALYSIS", nested=FALSE)
      ```

      <Frame>
        <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=bbe57a6e5a269a3291421899cbbb5654" alt="" data-og-width="1694" width="1694" data-og-height="1712" height="1712" data-path="images/create_udf_r_custom_name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=1c8cb2c1c1ad3a50d61d5bbddff9e482 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=69b44583db7858fb51aef174c9687e2d 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e64878144f327129b4cfb363cf60f712 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=5a7203d44ecffc992850bdce56bd0fb0 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=13195fc72350cd26e725307f3a8e8ff7 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/create_udf_r_custom_name.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=2848fabfdc2a327fbe4a6262354cc776 2500w" />
      </Frame>
    </Tip>

    **Using range arguments**

    Setting the `range_args` parameter tells Excel that the input of the function is a 2D range.  Without specifying this, Excel will show a `#CALC! Unliftable Array` error if a 2D range is passed into the UDF. Parameters specified as `range_args` will always be passed as a 2D array to the function, even if a single cell is passed in.

    Example usage of `range_args`:

    ```r R Range Example theme={null}
    my_custom_r_function <- function(data) {
        sum(data)
    }
    UDF.register(my_custom_r_function, range_args=c("data"))
    ```

    **Adding function documentation**

    To add documentation to your function, use the `doc` parameter:

    ```r R Documentation Example theme={null}
    my_custom_r_function <- function(x, y) {
        x ^ y
    }
    UDF.register(my_custom_r_function, doc="Computes x raised to the power of y.")
    ```
  </Accordion>
</AccordionGroup>

## Modifying workbook settings

While you can adjust the settings for running code in your workbook on a case-by-case basis when creating and editing code, you can also assign default settings from the **Settings** tab.

### Cell linking

<AccordionGroup>
  <Accordion title="Run Isolated">
    When a code cell is run in <Icon icon="link-simple-slash" iconType="light" /> **isolated** mode, its code runs independently of other cells. Variables defined within an isolated code cell can't be referenced by other code cells, and variables in other code cells likewise can't be referenced by the isolated code cell.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e28a4ac7b0c21c11b11f4947f303d02c" alt="Two code cells in isolated mode where the second cell cannot access variables from the first" data-og-width="1684" width="1684" data-og-height="948" height="948" data-path="images/cell_isolated_mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=cc926655d310e577b8d716461bab68a6 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=7d8061a23efbb3d233fde9e387c98420 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=bf8d89742812a7cbca0caeca37f2562b 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=2b3785789f9b826b69fe4b6e32e3a76a 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=b552bbb1e33607ce2b90415a01e889ee 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_isolated_mode.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=75b04f2cbcbd411a62405774e632172d 2500w" />
    </Frame>

    In the above image, the `output_of_B2` variable is defined in cell B2 and assigned the string `"I'm the B2 cell!"`. When this code is run in the B2 code cell, the B2 cell displays `"I'm the B2 cell!"`. However, since both cells are running in isolated mode, when `output_of_B2` is referenced in the B4 code cell, the B4 cell displays a `#VALUE!` error because B4 cannot access the variable in B2.

    **Using the `REF` function**

    You can bypass isolation rules as needed using the `REF` function to create a reference from one isolated code cell to another.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=0a6287dd90c0c73498e23d6557133461" alt="A code cell using the REF function to reference another cell's output" data-og-width="1704" width="1704" data-og-height="962" height="962" data-path="images/isolated_ref_cell.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=280&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=b56a71f44090f7a49c6cd2fa07fed96b 280w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=560&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=966d9ab29e616226cd6c3eeca069b4d9 560w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=840&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=78a913f30c04c90f1e3c5f2653d60824 840w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=1100&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=68fed1efc9937f1bbe78c4c4dd9b25c6 1100w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=1650&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=73d17eaa5428cff9c8aa85b61a8f937b 1650w, https://mintcdn.com/anaconda-29683c67/QCWY8EsGZWJYinOU/images/isolated_ref_cell.png?w=2500&fit=max&auto=format&n=QCWY8EsGZWJYinOU&q=85&s=21f7f82c541d536e9dd555243fd1ed02 2500w" />
    </Frame>

    In the above image, the B4 cell now includes a reference to the B2 cell, `REF("B2")`. When the B4 code cell is run, it returns the value of B2, `"I'm the B2 cell!"`. Changes to the B4 cell don't cause the B2 cell to recalculate, but changes to the B2 cell will cause the B4 cell to recalculate. Code cells can include multiple `REF` function references, and changes to any referenced cells (in this example, B2) will cause the referencing cells to recalculate (in this example, B4).

    **Working with code objects**

    If you reference a cell that's set to output a code object, the `REF` function will return an instance of that object in the referencing cell.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=a88c0a285d085c14ab3c12afe5120cb8" alt="A code cell referencing another cell that outputs a list object" data-og-width="1718" width="1718" data-og-height="968" height="968" data-path="images/code_object_isolated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=280&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=9701200f23ffc2a1393da4012ea21c45 280w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=560&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=33680dd70b91eb2c9cbe4fddbd252bf7 560w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=840&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=e99f2aff1f205424347212780948291c 840w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=1100&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=ad5325ba43d4a75b05fbe424db54083c 1100w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=1650&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=addd1a2ae6323b3829d2ced2df6235dc 1650w, https://mintcdn.com/anaconda-29683c67/6fJRxAwYs9izUc34/images/code_object_isolated.png?w=2500&fit=max&auto=format&n=6fJRxAwYs9izUc34&q=85&s=4d31cd9b92a61ba53043b2ad2e460514 2500w" />
    </Frame>

    In the above image, the B2 code cell is set to output a code object (in this case, a list). Because the output of B2 is a <Tooltip tip="A non-scalar value is a data structure that contains multiple values, such as a list, dictionary, or tuple.">non-scalar value</Tooltip>, we see `</> list` in B2. In the B4 code cell, we define a variable called `output_of_B2` and assign a `REF` function that references cell B2. The output mode for the B4 code cell is set to "Excel Values", so the list spills across multiple cells in the spreadsheet.

    **Benefits of isolated mode**

    The benefit of using the isolated mode is that referenced cells are not recalculated when changes are made to referencing cells. For complex processes, this allows you to:

    * separate code that doesn't change frequently from code you modify often.
    * reduce unnecessary recalculations of computationally intensive operations.
    * create a more modular approach to your data analysis.
    * improve performance when working with larger datasets.
  </Accordion>

  <Accordion title="Run Linked">
    When a code cell is run in <Icon icon="link-simple" iconType="light" /> **linked** mode, variables defined within it can be accessed by any other code cell also running in linked mode. When any linked mode cell is recalculated, all linked mode cells are recalculated. Linked cells run left-to-right, top-to-bottom, and can access objects defined in previously linked cells.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e4be8b9c4344868b197fef9062b442b6" alt="" data-og-width="1698" width="1698" data-og-height="952" height="952" data-path="images/cell_linked_mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=280&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=3d8e440d25369edf953f0400a37991c8 280w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=560&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=e52b875cdd5cabe82921e39e94cdb9bf 560w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=840&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=4c5f84e2322fb3ea57ef0a60e76c0053 840w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=1100&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=be2fc5900b83edc477e12dd6c17c6c1b 1100w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=1650&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=785ebaa8887db14cc357ee7716cc60be 1650w, https://mintcdn.com/anaconda-29683c67/9H-5W4tTlP7-Fn32/images/cell_linked_mode.png?w=2500&fit=max&auto=format&n=9H-5W4tTlP7-Fn32&q=85&s=29443653e2dcf1186f59fbccf9a50790 2500w" />
    </Frame>

    In the above image, both the B2 and B4 cell are running in linked mode. The `output_of_B2` variable is defined in cell B2 and assigned the string `"I'm the B2 cell!"`. When this code is run in the B2 code cell, the B2 cell displays `"I'm the B2 cell!"`. The `output_of_B2` variable is then referenced in the B4 code cell, causing the B4 cell to also display `"I'm the B2 cell!"`.

    **Benefits of linked mode**

    Linked mode is useful when:

    * you want to create a continuous workflow across multiple cells.
    * you need to share variables and objects between different parts of your analysis.
    * your code follows a linear execution path.
  </Accordion>
</AccordionGroup>

### Cell output

| Output            | Description                                                                                                                                                                                        |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Excel Values      | When outputting a DataFrame, array, list, and so on, the values will "spill" to fill the required space. If the spill were to overwrite cells containing data, the cell displays a `#SPILL` error. |
| Local Code Object | For certain object types, you can view the contents in a "Card View" by clicking the cell. You can reference this cell and the returned object like you would any other object.                    |

## Troubleshooting

If you encounter an issue that is not listed here, you can obtain support for Anaconda through the [Anaconda community forums](https://forum.anaconda.com) or by [opening a support ticket](https://support.anaconda.com/hc/en-us/requests/new?ticket_form_id=360000993773).

### Error installing functions

<AccordionGroup>
  <Accordion title="Cause">
    This error can occur when Excel loads the Anaconda Toolbox add-in and registers its custom functions. This error happens within Excel and cannot be resolved by the Anaconda Toolbox.
  </Accordion>

  <Accordion title="Solution">
    Close and reopen Excel. If the issue persists, uninstall the Anaconda Toolbox add-in, then reinstall.
  </Accordion>
</AccordionGroup>

# Datasets

export const Conflict = ({small}) => {
  if (small) {
    return <span className="inline_icon">
        <svg class="inline" width="16" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
          <path d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm8 11.5a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0Zm-3.8 0 1.15-1.15a.5.5 0 0 0-.7-.7l-1.15 1.14-1.15-1.14a.5.5 0 0 0-.7.7l1.14 1.15-1.14 1.15a.5.5 0 0 0 .7.7l1.15-1.14 1.15 1.14a.5.5 0 0 0 .7-.7l-1.14-1.15Z" fill="#dc3246"></path>
        </svg>
      </span>;
  }
  return <span className="inline_icon">
      <svg class="inline ___12fm75w f1w7gpdv fez10in fg4l7m0" aria-hidden="true" width="60" height="60" viewBox="0 0 22 23" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm8 11.5a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0Zm-3.8 0 1.15-1.15a.5.5 0 0 0-.7-.7l-1.15 1.14-1.15-1.14a.5.5 0 0 0-.7.7l1.14 1.15-1.14 1.15a.5.5 0 0 0 .7.7l1.15-1.14 1.15 1.14a.5.5 0 0 0 .7-.7l-1.14-1.15Z" fill="#dc3246"></path>
      </svg>
    </span>;
};

export const Synced = ({small}) => {
  if (small) {
    return <span className="inline_icon">
        <svg class="inline" width="16" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
          <path d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm8 11.5a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0Zm-2.85-1.85-2.65 2.64-.65-.64a.5.5 0 0 0-.7.7l1 1c.2.2.5.2.7 0l3-3a.5.5 0 0 0-.7-.7Z" fill="#0cca4a"></path>
        </svg>
      </span>;
  }
  return <span className="inline_icon">
      <svg class="inline" width="60" height="60" viewBox="0 0 22 23" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm8 11.5a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0Zm-2.85-1.85-2.65 2.64-.65-.64a.5.5 0 0 0-.7.7l1 1c.2.2.5.2.7 0l3-3a.5.5 0 0 0-.7-.7Z" fill="#0cca4a"></path>
      </svg>
    </span>;
};

export const Redownload = ({small}) => {
  if (small) {
    return <span className="inline_icon">
        <svg class="inline" width="16" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
          <path fill="currentColor" d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66A5.74 5.74 0 0 0 7.77 13H5.28A3.33 3.33 0 0 1 2 9.62a3.33 3.33 0 0 1 3.28-3.37h.07C5.6 3.9 7.18 2 10 2Zm3.5 16a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9Zm1.6-4.9L14 14.2v-2.7a.5.5 0 0 0-1 0v2.7l-1.1-1.1a.56.56 0 1 0-.8.8l2 2c.22.22.58.22.8 0l2-2a.56.56 0 1 0-.8-.8Z"></path>
        </svg>
      </span>;
  }
  return <span className="inline_icon">
      <svg class="inline" width="60" height="60" viewBox="0 0 22 23" xmlns="http://www.w3.org/2000/svg">
        <path fill="currentColor" d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66A5.74 5.74 0 0 0 7.77 13H5.28A3.33 3.33 0 0 1 2 9.62a3.33 3.33 0 0 1 3.28-3.37h.07C5.6 3.9 7.18 2 10 2Zm3.5 16a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9Zm1.6-4.9L14 14.2v-2.7a.5.5 0 0 0-1 0v2.7l-1.1-1.1a.56.56 0 1 0-.8.8l2 2c.22.22.58.22.8 0l2-2a.56.56 0 1 0-.8-.8Z"></path>
      </svg>
    </span>;
};

export const Download2 = ({small}) => {
  if (small) {
    return <span className="inline_icon">
        <svg class="inline" width="16" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
          <path d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm3.5 16a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9Zm1.6-4.9L14 14.2v-2.7a.5.5 0 0 0-1 0v2.7l-1.1-1.1a.56.56 0 1 0-.8.8l2 2c.22.22.58.22.8 0l2-2a.56.56 0 1 0-.8-.8Z" fill="currentColor"></path>
        </svg>
      </span>;
  }
  return <span className="inline_icon">
      <svg class="inline" width="60" height="60" viewBox="0 0 22 23" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm3.5 16a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9Zm1.6-4.9L14 14.2v-2.7a.5.5 0 0 0-1 0v2.7l-1.1-1.1a.56.56 0 1 0-.8.8l2 2c.22.22.58.22.8 0l2-2a.56.56 0 1 0-.8-.8Z" fill="currentColor"></path>
      </svg>
    </span>;
};

export const Reupload = ({small}) => {
  if (small) {
    return <span className="inline_icon">
        <svg class="inline" width="16" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
          <path fill="currentColor" d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm3.5 7a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm1.6 4.9a.56.56 0 1 0 .8-.8l-2-2a.56.56 0 0 0-.8 0l-2 2a.56.56 0 1 0 .8.8l1.1-1.1v2.7a.5.5 0 0 0 1 0v-2.7l1.1 1.1Z"></path>
        </svg>
      </span>;
  }
  return <span className="inline_icon">
      <svg class="inline" width="60" height="60" viewBox="0 0 22 23" xmlns="http://www.w3.org/2000/svg">
        <path fill="currentColor" d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm3.5 7a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm1.6 4.9a.56.56 0 1 0 .8-.8l-2-2a.56.56 0 0 0-.8 0l-2 2a.56.56 0 1 0 .8.8l1.1-1.1v2.7a.5.5 0 0 0 1 0v-2.7l1.1 1.1Z"></path>
      </svg>
    </span>;
};

export const Upload2 = ({small}) => {
  if (small) {
    return <span className="inline_icon">
        <svg class="inline" width="16" height="16" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
          <path fill="currentColor" d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm3.5 7a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm1.6 4.9a.56.56 0 1 0 .8-.8l-2-2a.56.56 0 0 0-.8 0l-2 2a.56.56 0 1 0 .8.8l1.1-1.1v2.7a.5.5 0 0 0 1 0v-2.7l1.1 1.1Z"></path>
        </svg>
      </span>;
  }
  return <span className="inline_icon">
      <svg class="inline" width="60" height="60" viewBox="0 0 22 23" xmlns="http://www.w3.org/2000/svg">
        <path fill="currentColor" d="M10 2c2.82 0 4.41 1.92 4.65 4.25h.07a3.33 3.33 0 0 1 3.27 3.66c-.32-.4-.7-.76-1.12-1.07a2.3 2.3 0 0 0-2.15-1.6h-.07a1 1 0 0 1-1-.9C13.45 4.33 12.11 3 10 3S6.55 4.32 6.35 6.35a1 1 0 0 1-1 .9h-.07A2.33 2.33 0 0 0 3 9.62 2.33 2.33 0 0 0 5.28 12h2.67c-.09.32-.15.66-.18 1H5.28A3.33 3.33 0 0 1 2 9.62c0-1.8 1.37-3.27 3.1-3.37h.25C5.6 3.9 7.18 2 10 2Zm3.5 7a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm1.6 4.9a.56.56 0 1 0 .8-.8l-2-2a.56.56 0 0 0-.8 0l-2 2a.56.56 0 1 0 .8.8l1.1-1.1v2.7a.5.5 0 0 0 1 0v-2.7l1.1 1.1Z"></path>
      </svg>
    </span>;
};

Datasets enable you to securely upload and update datasets in Anaconda's cloud storage. You can then provide access to other users, as well as import your datasets to a separate workbook to continue your data analysis from any machine, anytime.

## Understanding datasets

Let's take a look at the different elements and tabs within Datasets.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_anatomy.png?fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=cb5cab0b418e31b93342f9c05b4cb67d" alt="" data-og-width="540" width="540" data-og-height="800" height="800" data-path="images/dataset_anatomy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_anatomy.png?w=280&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=f94b7fde37142f7fd30c42d7a1fcda64 280w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_anatomy.png?w=560&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=f82c6baf59d2082fdde9ce84a54215ba 560w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_anatomy.png?w=840&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=067d45796961ca9f52a876bb052b5d5b 840w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_anatomy.png?w=1100&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=4da8a2386f1aca14fa7e4a6cf04bf73e 1100w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_anatomy.png?w=1650&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=fb8cef45d76420e16c568389ae5eb568 1650w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_anatomy.png?w=2500&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=693c7041a9ec3b946bf9e319a9c348cd 2500w" />
</Frame>

<Steps>
  <Step title="Cloud">
    Shows all projects and project contents
  </Step>

  <Step title="Connections">
    Displays datasets previously uploaded to or downloaded from Anaconda's cloud storage
  </Step>

  <Step title="New Project">
    Create a new project to store and share datasets (sheets and tables)
  </Step>

  <Step title="New Dataset">
    Create a new dataset and assign it to a project
  </Step>

  <Step title="Filters">
    Apply filters to efficiently locate data in your catalog
  </Step>

  <Step title="My Datasets">
    A collection of all your cloud projects and their nested datasets
  </Step>

  <Step title="User Datasets">
    Projects to which you have access, owned by other individuals
  </Step>

  <Step title="Organization Datasets">
    Projects to which you have access, owned by organizations
  </Step>

  <Step title="Status Icons">
    Indicates the [connection status](#understanding-status-icons) of your dataset
  </Step>
</Steps>

## Creating a project

When you first access Datasets, you are prompted to create a new project. You can think of projects as folders for storing your datasets.

Create a project at any time using the following steps:

1. From the **Cloud** tab, click **+ New Project**.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_new_project.png?fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=aa10558a3e5bbcaac20e196515fc0987" alt="" data-og-width="1092" width="1092" data-og-height="2050" height="2050" data-path="images/dataset_new_project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_new_project.png?w=280&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=81aab0bb1e56d2c3ad45fbf903f90841 280w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_new_project.png?w=560&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=5f1b3dc16377a3245786b3344a332475 560w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_new_project.png?w=840&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=e843a9869c3a89d8ed70e0e3a2595315 840w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_new_project.png?w=1100&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=4aa5802e900bfd8b1009c47cddf49393 1100w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_new_project.png?w=1650&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=1bbce547fbc6581cdfd4ec2e5b1780d9 1650w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_new_project.png?w=2500&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=7ff4b40d107b61140507db33dd7ca1ea 2500w" />
   </Frame>

2. Enter a unique title for your project and an optional description.

3. Designate the project owner(s) for your project. By default, you are set as the only project owner.

   <Note>
     Administrators and project owners are the only users allowed to edit projects. Anaconda.com organization administrators have full permissions for any projects owned by their organization.
   </Note>

4. (Optional) Provide access to your project by [inviting users](#sharing-a-project-with-other-users) from one of your organizations.

5. Click **Save**.

## Sharing a project with other users

You can share a project to collaborate with others in your organization when creating a new project, or at any time using the following steps:

1. From the **Cloud** tab, click <Icon icon="ellipsis-vertical" iconType="solid" /> actions beside a project for which you have edit permissions, then click **Edit**.
2. Provide access to your project by inviting users from one of your [organizations](https://anaconda.com/app/profile/organizations).

   1. Under **Your Organizations**, select an organization.
   2. Under **Organization Users**, select a user to share your project with.
   3. Choose whether the user should have read or write access to your project.
3. Click **Save**.

### Permissions

Access to projects and the actions you can perform in them are determined by your permission level for the project. By default, you as the owner of your project have admin permissions; for projects owned by an organization, the admins of that organization have admin permissions for that project.

| Permission level | Actions                               |
| :--------------- | :------------------------------------ |
| Read             | View, download                        |
| Edit             | View, download, upload                |
| Admin            | View, download, upload, share, delete |

## Uploading data

Protect your local datasets and increase their accessibility by saving them in cloud storage. If you experience hardware failure, or need to work on a different device, your projects will be right where you left them!

Upload sheets and tables to your projects using the following steps:

1. From the **Cloud** tab, click **+ New Dataset**.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload.png?fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=ce1301cf5c8164eddcf5668fbed15db1" alt="" data-og-width="556" width="556" data-og-height="800" height="800" data-path="images/dataset_upload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload.png?w=280&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=81930e4fd7c3ed68686fffa993061a40 280w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload.png?w=560&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=e09ac3931a9826e28bb04c02105fc438 560w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload.png?w=840&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=dc6aa6ee3519a311763137fc167d4dac 840w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload.png?w=1100&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=7a0fab1b8a3781237f967ee2a62dbd62 1100w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload.png?w=1650&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=395ec06a8bdf2a59606ea13fb739bfe3 1650w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload.png?w=2500&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=0961296c877c109d7ab648d3f680bc8e 2500w" />
   </Frame>

2. Under **Data**, choose a range of data manually, a specific table, or an entire sheet.

3. Under **Project**, select a project to house your dataset.

4. Under **Dataset Title**, provide a title for your dataset.

5. Complete the upload by clicking **Save to Cloud**.

You can now see the established connection between your dataset and Anaconda's cloud storage on the **Connections** tab.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload_result.png?fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=864748c7328fc7b866efd2db4db09371" alt="" data-og-width="557" width="557" data-og-height="800" height="800" data-path="images/dataset_upload_result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload_result.png?w=280&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=b568cb28b227d360c76a26d3b48b2223 280w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload_result.png?w=560&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=54fc79326d6f76b06f50a0e1f375a3f0 560w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload_result.png?w=840&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=6fdb312c04570d3251b5930ca1c2615e 840w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload_result.png?w=1100&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=e916ba21923036d6af606bbc52a66f2c 1100w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload_result.png?w=1650&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=a2c2cfac385d8b64ea9156313931b951 1650w, https://mintcdn.com/anaconda-29683c67/atV1FF4bOzhiwIx6/images/dataset_upload_result.png?w=2500&fit=max&auto=format&n=atV1FF4bOzhiwIx6&q=85&s=3f38c2d2149c4ebda679f864afc1a0be 2500w" />
</Frame>

When you make changes to the dataset, **re-upload** it to update the dataset stored in the cloud.

## Downloading data

If another user shares a project with you, or if you've uploaded a dataset in another workbook or Anaconda Notebook, **download** appears beside that dataset. Datasets can be downloaded as either an Excel range reference or as an Anaconda Code object.

<Tabs>
  <Tab title="Excel Range">
    To download a dataset as an Excel range reference:

    1. Click **download** beside the dataset you want to download.
    2. Under **Workbook Placement**, select the sheet where you want to insert the data.
    3. Complete the download by clicking **Download to Workbook**.

    The data is now available in the selected sheet.
  </Tab>

  <Tab title="Anaconda Code object">
    To download a dataset as an Anaconda Code object:

    1. Click **download** beside the dataset you want to download.
    2. Select **Import as Anaconda Code object**.

       <Note>
         If you're unable to select **Import as Anaconda Code object**, go to <Icon icon="gear" iconType="solid" /> **Settings** and, under **Generate Toolbox code as:**, select **Anaconda Code (=ANACONDA.CODE).**

         <Frame>
           <img src="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/generate_as_anaconda_code.png?fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=5c7405100697762c86d0b68a43445670" alt="" data-og-width="1438" width="1438" data-og-height="684" height="684" data-path="images/generate_as_anaconda_code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/generate_as_anaconda_code.png?w=280&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=3435fd914dece65013aee11ea8bead7e 280w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/generate_as_anaconda_code.png?w=560&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=c75b5c246de94c89e0f8f05730bfe95f 560w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/generate_as_anaconda_code.png?w=840&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=a14e0dfd1991c96bb9832736252357f1 840w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/generate_as_anaconda_code.png?w=1100&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=eda1e8da60a7636701e5d158f45dfa89 1100w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/generate_as_anaconda_code.png?w=1650&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=14044f7db9686c41970447f94e835d76 1650w, https://mintcdn.com/anaconda-29683c67/opbTXGcYjx4zM8zO/images/generate_as_anaconda_code.png?w=2500&fit=max&auto=format&n=opbTXGcYjx4zM8zO&q=85&s=07c2360021872871f4b862a99a98ec59 2500w" />
         </Frame>
       </Note>
    3. Click **Click to select**.
    4. Select an empty cell.
    5. Click **OK** in the Select Data dialog.
    6. Click **Download to Workbook**.

    The selected cell will display <Icon icon="cloud" iconType="regular" /> **PyScript Data**. Click <Icon icon="cloud" iconType="regular" /> to see details about the object.
  </Tab>
</Tabs>

## Understanding status icons

Status icons appear by each dataset. Click the icons to perform the following functions:

| Icon           | Name        | Function                                                                                                                                           |
| :------------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| <Upload2 />    | Upload      | Click to upload a dataset in your workbook to Anaconda's cloud storage.                                                                            |
| <Reupload />   | Re-upload   | Click to re-upload the dataset in your workbook to Anaconda's cloud storage.                                                                       |
| <Download2 />  | Download    | Click to download a dataset from Anaconda's cloud storage to your workbook.                                                                        |
| <Redownload /> | Re-download | The dataset on Anaconda's cloud storage has been updated. Click to update the dataset in your Excel workbook with these changes.                   |
| <Synced />     | Synced      | The dataset in your Excel workbook is up-to-date with the dataset in Anaconda's cloud storage.                                                     |
| <Conflict />   | Conflict    | The dataset on Anaconda's cloud storage has been updated and now conflicts with the dataset in your Excel Workbook. Click to resolve the conflict. |



# Code Snippets

Code Snippets enable you to securely upload reusable blocks of code to Anaconda's cloud storage. You can then provide access to other users, as well as import your code snippets to separate workbooks to repeat your efforts from any machine, anytime.

## Understanding connections

Let's take a look at the different elements within Code Snippets.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=c6d95ba479c3d7989fe9a6944cc0e79b" alt="" data-og-width="534" width="534" data-og-height="800" height="800" data-path="images/snippets_anatomy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=2acba1e20def60451a5e1987384bb778 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=3a0c730c823bdba09eb94f31bc6cab40 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=b18d7f882f79ed6fea7735c71de91385 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=b6fea5c94c31a8044643e4da8488d856 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=86a45f32636aac62716350a907620e17 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=03dd2933144d2be8180fb9bf83d8f881 2500w" />
</Frame>

<Steps>
  <Step title="New Project">
    Create a new project to store and share snippets
  </Step>

  <Step title="New Snippet">
    Create and store a new snippet in Anaconda's cloud storage
  </Step>

  <Step title="Filters">
    Apply filters to efficiently locate snippets in your catalog
  </Step>

  <Step title="My Snippets">
    A collection of all your cloud projects and their nested snippets
  </Step>

  <Step title="User Snippets">
    Projects to which you have access, owned by other individuals
  </Step>

  <Step title="Organization Snippets">
    Projects to which you have access, owned by organizations
  </Step>

  <Step title="Project actions">
    Edit, delete, and [share projects](#sharing-a-snippet)
  </Step>

  <Step title="Snippet actions">
    Edit and delete snippets
  </Step>

  <Step title="Running snippets">
    Multiple methods for [adding and running snippets in a workbook](#adding-snippets-to-a-workbook)
  </Step>
</Steps>

## Create a project

When you first access Code Snippets, you are prompted to create a new project. You can think of projects as folders for storing your snippets.

You must create a project before uploading your first snippet. Create a project at any time using the following steps:

1. Click **+ New Project**.

2. Enter a unique title for your project and an optional description.

3. Designate the project owner(s) for your project. By default, you are set as the only project owner.

   <Note>
     Administrators and project owners are the only users allowed to edit projects. Anaconda.com organization administrators have full permissions for any projects owned by their organization.
   </Note>

4. (Optional) Provide access to your project by inviting users from one of your organizations.

5. Click **Save**.

## Sharing a snippet

You can share a snippet with others in your organization by sharing the project containing that snippet. This can be done as you're creating a new project or at any time using the following steps:

1. Click actions beside a project for which you have edit permissions, then click <Icon icon="pencil" iconType="light" /> **Edit**.
2. Provide access to your project by inviting users from one of your [organizations](https://anaconda.com/app/profile/organizations).

   1. Under **Your Organizations**, select an organization.
   2. Under **Organization Users**, select a user to share your project with.
   3. Choose whether the user should have read or write access to your project.
3. Click **Save**.

## Uploading a snippet

With a project in Anaconda's cloud storage, you can now create a snippet and upload it to that project. This can be done from Code Snippets or, if you want to save code generated while creating visualizations of your data, you can upload a snippet from [Visualize with Python](./visualize).

<Tabs>
  <Tab title="Upload from Code Snippets">
    1. Click **+ New Snippet**.
    2. Under **Project**, select an existing project to house your snippet.
    3. Under **Snippet Title**, provide a title for your snippet.
    4. Select a language, then enter your code in the code editor. Alternatively, click **+ Add From Grid** to add existing code from your workbook.
    5. Click **Save to Cloud**.

    Your snippet appears in its assigned project folder.
  </Tab>

  <Tab title="Upload from Visualize with Python">
    When working in Visualize with Python, Anaconda Toolbox writes code to render your data as a visualization. You can then open this code in Code Snippets to edit and save to Anaconda's cloud storage using the following steps:

    1. From the Toolbox home screen, open **Visualize with Python**.

    2. Click **New Chart**, then select a chart type.

    3. Select the source range and adjust the chart settings from the **Setup** tab, customize the chart from the **Design** tab, and then open the **Code** tab.

    4. Click <Icon icon="rectangle-code" iconType="regular" /> **Save as code snippet** to open the code in Code Snippets.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=c43c7d207802a7b65227362aa973e0fd" alt="" data-og-width="535" width="535" data-og-height="800" height="800" data-path="images/snippets_visualize.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=e649649a63fff8080c8f9637650b9887 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=de305391a3feb6f6d975c15d1a57a4a8 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=2f7feb3a15309125e8ac13751472e25a 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=8cfd56f3b927491983be90776f411be8 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fd4b5a0b79a5e4b9392605e8fc589f63 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=765843202c5339529fe319d2e7b9c1f6 2500w" />
       </Frame>

    5. Select a project to upload the snippet to, then provide a title.

    6. If needed, edit the code to suit multiple use cases by converting labels to variables, parameterizing functions, and so on.

    7. Click **Save to Cloud**.

    Your snippet appears in its assigned project folder.
  </Tab>
</Tabs>

## Adding snippets to a workbook

When you're ready to make use of your saved snippets, import them to a workbook using the following steps:

1. Expand the <Icon icon="chevron-down" iconType="regular" /> dropdown beside your snippet. A preview of your snippet appears.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=9abe9d4f7d3fa60c4bfb677c697e7e23" alt="" data-og-width="535" width="535" data-og-height="800" height="800" data-path="images/snippets_add.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=31572408b78e273bd93e2f2459c8fc69 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=eaf872d850f0f5cc1d431297ea17975d 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=0b45bfd5e7ef00ea1d0a281558744876 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=965b0ddcfa033469136434aa971cf7fd 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=33d635e20149cbfa722967cbe37e3a74 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fe961a917c213d3afdeff26de3d60149 2500w" />
   </Frame>

2. You can now import your snippet in one of two ways:

<Tabs>
  <Tab title="Run in cell">
    1) Click <Icon icon="play" iconType="regular" /> **Run in cell**.
    2) Select the cell where you want to insert the snippet, then click **OK**.
  </Tab>

  <Tab title="Copy code">
    1. Click <Icon icon="copy" iconType="regular" /> **Copy** to copy the snippet to your clipboard.
    2. In an open cell, type `=PY`, press Tab, and then paste your snippet in the green PY formula bar.
    3. Use Ctrl+Enter (Windows)/Ctrl+Return (Mac) to run the code.
  </Tab>
</Tabs>

## Editing a snippet

Changes made to a saved snippet in a workbook will not automatically update that snippet in Anaconda's cloud storage. Instead, you must make changes to the snippet directly within the Anaconda Toolbox extension.

1. Expand the <Icon icon="chevron-down" iconType="regular" /> dropdown beside your snippet. A preview of your snippet appears.

2. Click <Icon icon="pencil" iconType="light" /> **Edit**.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fb7c332b8d483f59f4180e853e49e088" alt="" data-og-width="535" width="535" data-og-height="800" height="800" data-path="images/snippets_edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=17d1b2a2f404653d348cb1d77eb028a5 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=718c162751498c136e90976eb70bfe9d 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=75de5602b987026220832e1e27b45884 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=e2fff73d06c1e41d8635bedbaa75ee20 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fe22c18d7e4ad9cd1675da70b07900af 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=efaaba09fe8df35a2d504e5f9315b0fd 2500w" />
   </Frame>

3. Adjust your snippet, then click **Save to Cloud**.

   <Note>
     Changing the title of your snippet will create a new snippet, rather than updating the existing one.
   </Note>

# Code Snippets

Code Snippets enable you to securely upload reusable blocks of code to Anaconda's cloud storage. You can then provide access to other users, as well as import your code snippets to separate workbooks to repeat your efforts from any machine, anytime.

## Understanding connections

Let's take a look at the different elements within Code Snippets.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=c6d95ba479c3d7989fe9a6944cc0e79b" alt="" data-og-width="534" width="534" data-og-height="800" height="800" data-path="images/snippets_anatomy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=2acba1e20def60451a5e1987384bb778 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=3a0c730c823bdba09eb94f31bc6cab40 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=b18d7f882f79ed6fea7735c71de91385 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=b6fea5c94c31a8044643e4da8488d856 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=86a45f32636aac62716350a907620e17 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_anatomy.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=03dd2933144d2be8180fb9bf83d8f881 2500w" />
</Frame>

<Steps>
  <Step title="New Project">
    Create a new project to store and share snippets
  </Step>

  <Step title="New Snippet">
    Create and store a new snippet in Anaconda's cloud storage
  </Step>

  <Step title="Filters">
    Apply filters to efficiently locate snippets in your catalog
  </Step>

  <Step title="My Snippets">
    A collection of all your cloud projects and their nested snippets
  </Step>

  <Step title="User Snippets">
    Projects to which you have access, owned by other individuals
  </Step>

  <Step title="Organization Snippets">
    Projects to which you have access, owned by organizations
  </Step>

  <Step title="Project actions">
    Edit, delete, and [share projects](#sharing-a-snippet)
  </Step>

  <Step title="Snippet actions">
    Edit and delete snippets
  </Step>

  <Step title="Running snippets">
    Multiple methods for [adding and running snippets in a workbook](#adding-snippets-to-a-workbook)
  </Step>
</Steps>

## Create a project

When you first access Code Snippets, you are prompted to create a new project. You can think of projects as folders for storing your snippets.

You must create a project before uploading your first snippet. Create a project at any time using the following steps:

1. Click **+ New Project**.

2. Enter a unique title for your project and an optional description.

3. Designate the project owner(s) for your project. By default, you are set as the only project owner.

   <Note>
     Administrators and project owners are the only users allowed to edit projects. Anaconda.com organization administrators have full permissions for any projects owned by their organization.
   </Note>

4. (Optional) Provide access to your project by inviting users from one of your organizations.

5. Click **Save**.

## Sharing a snippet

You can share a snippet with others in your organization by sharing the project containing that snippet. This can be done as you're creating a new project or at any time using the following steps:

1. Click actions beside a project for which you have edit permissions, then click <Icon icon="pencil" iconType="light" /> **Edit**.
2. Provide access to your project by inviting users from one of your [organizations](https://anaconda.com/app/profile/organizations).

   1. Under **Your Organizations**, select an organization.
   2. Under **Organization Users**, select a user to share your project with.
   3. Choose whether the user should have read or write access to your project.
3. Click **Save**.

## Uploading a snippet

With a project in Anaconda's cloud storage, you can now create a snippet and upload it to that project. This can be done from Code Snippets or, if you want to save code generated while creating visualizations of your data, you can upload a snippet from [Visualize with Python](./visualize).

<Tabs>
  <Tab title="Upload from Code Snippets">
    1. Click **+ New Snippet**.
    2. Under **Project**, select an existing project to house your snippet.
    3. Under **Snippet Title**, provide a title for your snippet.
    4. Select a language, then enter your code in the code editor. Alternatively, click **+ Add From Grid** to add existing code from your workbook.
    5. Click **Save to Cloud**.

    Your snippet appears in its assigned project folder.
  </Tab>

  <Tab title="Upload from Visualize with Python">
    When working in Visualize with Python, Anaconda Toolbox writes code to render your data as a visualization. You can then open this code in Code Snippets to edit and save to Anaconda's cloud storage using the following steps:

    1. From the Toolbox home screen, open **Visualize with Python**.

    2. Click **New Chart**, then select a chart type.

    3. Select the source range and adjust the chart settings from the **Setup** tab, customize the chart from the **Design** tab, and then open the **Code** tab.

    4. Click <Icon icon="rectangle-code" iconType="regular" /> **Save as code snippet** to open the code in Code Snippets.

       <Frame>
         <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=c43c7d207802a7b65227362aa973e0fd" alt="" data-og-width="535" width="535" data-og-height="800" height="800" data-path="images/snippets_visualize.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=e649649a63fff8080c8f9637650b9887 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=de305391a3feb6f6d975c15d1a57a4a8 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=2f7feb3a15309125e8ac13751472e25a 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=8cfd56f3b927491983be90776f411be8 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fd4b5a0b79a5e4b9392605e8fc589f63 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_visualize.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=765843202c5339529fe319d2e7b9c1f6 2500w" />
       </Frame>

    5. Select a project to upload the snippet to, then provide a title.

    6. If needed, edit the code to suit multiple use cases by converting labels to variables, parameterizing functions, and so on.

    7. Click **Save to Cloud**.

    Your snippet appears in its assigned project folder.
  </Tab>
</Tabs>

## Adding snippets to a workbook

When you're ready to make use of your saved snippets, import them to a workbook using the following steps:

1. Expand the <Icon icon="chevron-down" iconType="regular" /> dropdown beside your snippet. A preview of your snippet appears.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=9abe9d4f7d3fa60c4bfb677c697e7e23" alt="" data-og-width="535" width="535" data-og-height="800" height="800" data-path="images/snippets_add.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=31572408b78e273bd93e2f2459c8fc69 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=eaf872d850f0f5cc1d431297ea17975d 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=0b45bfd5e7ef00ea1d0a281558744876 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=965b0ddcfa033469136434aa971cf7fd 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=33d635e20149cbfa722967cbe37e3a74 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_add.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fe961a917c213d3afdeff26de3d60149 2500w" />
   </Frame>

2. You can now import your snippet in one of two ways:

<Tabs>
  <Tab title="Run in cell">
    1) Click <Icon icon="play" iconType="regular" /> **Run in cell**.
    2) Select the cell where you want to insert the snippet, then click **OK**.
  </Tab>

  <Tab title="Copy code">
    1. Click <Icon icon="copy" iconType="regular" /> **Copy** to copy the snippet to your clipboard.
    2. In an open cell, type `=PY`, press Tab, and then paste your snippet in the green PY formula bar.
    3. Use Ctrl+Enter (Windows)/Ctrl+Return (Mac) to run the code.
  </Tab>
</Tabs>

## Editing a snippet

Changes made to a saved snippet in a workbook will not automatically update that snippet in Anaconda's cloud storage. Instead, you must make changes to the snippet directly within the Anaconda Toolbox extension.

1. Expand the <Icon icon="chevron-down" iconType="regular" /> dropdown beside your snippet. A preview of your snippet appears.

2. Click <Icon icon="pencil" iconType="light" /> **Edit**.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fb7c332b8d483f59f4180e853e49e088" alt="" data-og-width="535" width="535" data-og-height="800" height="800" data-path="images/snippets_edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=280&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=17d1b2a2f404653d348cb1d77eb028a5 280w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=560&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=718c162751498c136e90976eb70bfe9d 560w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=840&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=75de5602b987026220832e1e27b45884 840w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=1100&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=e2fff73d06c1e41d8635bedbaa75ee20 1100w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=1650&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=fe22c18d7e4ad9cd1675da70b07900af 1650w, https://mintcdn.com/anaconda-29683c67/u4MsRLDCM8Pedgc_/images/snippets_edit.png?w=2500&fit=max&auto=format&n=u4MsRLDCM8Pedgc_&q=85&s=efaaba09fe8df35a2d504e5f9315b0fd 2500w" />
   </Frame>

3. Adjust your snippet, then click **Save to Cloud**.

   <Note>
     Changing the title of your snippet will create a new snippet, rather than updating the existing one.
   </Note>



# Data Science & AI Workbench

Workbench is an enterprise-ready, secure and scalable data science platform that empowers teams to govern data science assets, collaborate and deploy their data science projects.

With Workbench, you can do the following:

* **Develop**: ML/AI pipelines in a central development environment that scales from laptops to thousands of nodes
* **Govern**: Complete reproducibility from laptop to cluster with the ability to configure access control
* **Automate**: Model training and deployment on scalable, container-based infrastructure

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/kBuj3mPdZoBk8YoG/images/workbench_arc.png?fit=max&auto=format&n=kBuj3mPdZoBk8YoG&q=85&s=3f02d7bccb284b1a3a65ac5241e0a77b" alt="" data-og-width="2176" width="2176" data-og-height="1052" height="1052" data-path="images/workbench_arc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/kBuj3mPdZoBk8YoG/images/workbench_arc.png?w=280&fit=max&auto=format&n=kBuj3mPdZoBk8YoG&q=85&s=88e005c6f320a7802aab0efbc1691864 280w, https://mintcdn.com/anaconda-29683c67/kBuj3mPdZoBk8YoG/images/workbench_arc.png?w=560&fit=max&auto=format&n=kBuj3mPdZoBk8YoG&q=85&s=d3abe559246e3e5de7ed37030d88dfcf 560w, https://mintcdn.com/anaconda-29683c67/kBuj3mPdZoBk8YoG/images/workbench_arc.png?w=840&fit=max&auto=format&n=kBuj3mPdZoBk8YoG&q=85&s=d8b0d36128cea3b2b5529c4d1f364493 840w, https://mintcdn.com/anaconda-29683c67/kBuj3mPdZoBk8YoG/images/workbench_arc.png?w=1100&fit=max&auto=format&n=kBuj3mPdZoBk8YoG&q=85&s=f6871d09c10c2d72c04927d35d25ab65 1100w, https://mintcdn.com/anaconda-29683c67/kBuj3mPdZoBk8YoG/images/workbench_arc.png?w=1650&fit=max&auto=format&n=kBuj3mPdZoBk8YoG&q=85&s=40fe10e7c39c757eb0a67bd12ae71de3 1650w, https://mintcdn.com/anaconda-29683c67/kBuj3mPdZoBk8YoG/images/workbench_arc.png?w=2500&fit=max&auto=format&n=kBuj3mPdZoBk8YoG&q=85&s=6897664de23b387647f2fb801212df62 2500w" />
</Frame>

# Using Workbench

<CardGroup cols={3}>
  <Card title="Projects" href="/data-science/latest/data-science-workflows/projects/main" icon="square-kanban" />

  <Card title="Working with channels and packages" href="/data-science/latest/data-science-workflows/packages/main" icon="cube" />

  <Card title="Using installers, parcels and management packs" href="/data-science/latest/data-science-workflows/installers" icon="download" />

  <Card title="Working with data" href="/data-science/latest/data-science-workflows/data/main" icon="database" />

  <Card title="Deployments" href="/data-science/latest/data-science-workflows/deployments/main" icon="code-commit" />

  <Card title="Schedules" href="/data-science/latest/data-science-workflows/schedules" icon="calendar" />

  <Card title="Using GPUs in sessions and deployments" href="/data-science/latest/data-science-workflows/gpu" icon="code-fork" />

  <Card title="User settings" href="/data-science/latest/data-science-workflows/user-settings" icon="user" />

  <Card title="Secrets" href="/data-science/latest/data-science-workflows/secrets" icon="key" />

  <Card title="Configuring user access to external version control" href="/data-science/latest/data-science-workflows/external-repo-user" icon="code-compare" />

  <Card title="Visualizations and dashboards" href="/data-science/latest/data-science-workflows/viz" icon="gauge" />

  <Card title="Machine learning and deep learning" href="/data-science/latest/data-science-workflows/ml-deep-learn/main" icon="head-side-gear" />
</CardGroup>

# Using Workbench

<CardGroup cols={3}>
  <Card title="Projects" href="/data-science/latest/data-science-workflows/projects/main" icon="square-kanban" />

  <Card title="Working with channels and packages" href="/data-science/latest/data-science-workflows/packages/main" icon="cube" />

  <Card title="Using installers, parcels and management packs" href="/data-science/latest/data-science-workflows/installers" icon="download" />

  <Card title="Working with data" href="/data-science/latest/data-science-workflows/data/main" icon="database" />

  <Card title="Deployments" href="/data-science/latest/data-science-workflows/deployments/main" icon="code-commit" />

  <Card title="Schedules" href="/data-science/latest/data-science-workflows/schedules" icon="calendar" />

  <Card title="Using GPUs in sessions and deployments" href="/data-science/latest/data-science-workflows/gpu" icon="code-fork" />

  <Card title="User settings" href="/data-science/latest/data-science-workflows/user-settings" icon="user" />

  <Card title="Secrets" href="/data-science/latest/data-science-workflows/secrets" icon="key" />

  <Card title="Configuring user access to external version control" href="/data-science/latest/data-science-workflows/external-repo-user" icon="code-compare" />

  <Card title="Visualizations and dashboards" href="/data-science/latest/data-science-workflows/viz" icon="gauge" />

  <Card title="Machine learning and deep learning" href="/data-science/latest/data-science-workflows/ml-deep-learn/main" icon="head-side-gear" />
</CardGroup>

# Project configurations

In Data Science & AI Workbench, projects are structured around a core configuration file called `anaconda-project.yml`. This file is crucial for orchestrating a project’s components for deployment and ensuring operational consistency over time. There are several parameters that must be included within each project’s `anaconda-project.yml` file to ensure that it operates as intended:

* **Packages** - You must specify all conda or pip packages the project requires to function in its `anaconda-project.yml` file. By default, Workbench is configured to use packages from its internal repository to create project environments. However, it is possible to use packages from external repositories.
* **Environment** - You must define at least one named environment to accurately manage the project’s packages and their dependencies, ensuring stability across different settings. Projects use template environments when they are initially created, which can be updated or replaced. For more information about template environments, see [Configuring persistent environments and sample projects](../../admin/custom_env_proj).
* **Commands** - You must define at least one command to properly deploy and run jobs for your project in its intended environment.
* **Environmental variables** - If necessary, set up the required environment variables needed to control how your project interacts with external resources and services.

<Warning>
  It is possible to edit a project’s `anaconda-project.yml` file manually to add the required configurations; however, this method is prone to human error, especially for users who are unfamiliar with `.yml` file formatting.

  Instead, Anaconda recommends using `anaconda-project` commands from a terminal within your project to update its configurations when possible. For more information about `anaconda-project`, see the [official documentation here](https://anaconda-project.readthedocs.io/en/latest/).

  *All* `anaconda-project` commands *must* be run from the `lab_launch` environment! Enter the `lab_launch` environment by running the following command in a project terminal:

  ```sh  theme={null}
  conda activate lab_launch
  ```
</Warning>

Once you are finished configuring your project, Anaconda recommends that you [add a lock file](#locking-project-configurations) to your project to ensure its reproducibility across different environments at scale.

## Configuring project environments

The conda environments in [standard project templates](./project-templates) are pre-solved to reduce initialization time when additional packages are added. However, you might want to create an environment specifically for your project.

To create a new environment with specific packages and add it to your project:

1. Create a new project.

2. Start a session.

3. Open a terminal within your session editor.

4. Create an environment and include the packages you need for it by running the following command:

   ```sh  theme={null}
    # Replace <ENV_NAME> with the name of the environment you are creating to add to your project's configuration
    # Replace <PACKAGE_NAME> with the name of the packages you want to add to your project's configuration
    anaconda-project add-env-spec --name <ENV_NAME> <PACKAGE_NAME> <PACKAGE_NAME>
   ```

5. Remove the template environment that you used to create your project by running the following command:

   ```sh  theme={null}
    # Replace <TEMPLATE_ENV> with the name of the template environment you used to initially create the project
    anaconda-project remove-env-spec --name <TEMPLATE_ENV>
   ```

6. [Commit and push your updates to the project](./collaborate#committing-and-pushing-changes).

7. Stop and re-start the project.

<Warning>
  To edit and run notebooks in Jupyter Notebook or JupyterLab, you must include the `notebook` package in your project’s environment.

  <Accordion title="Verify your environment is initialized for notebooks">
    1. Open a terminal within your session editor.
    2. Run the following commands:

       ```sh  theme={null}
       cd /opt/continuum/
       ls
       ```

       If the environment is being initialized, you will see a file named `preparing`. Once initialization is complete, you will see a file named `prepare.log`. To troubleshoot environment initialization, view the log from the terminal by running the following command:

       ```sh  theme={null}
       cat /opt/continuum/prepare.log
       ```
  </Accordion>
</Warning>

## Configuring project packages

Adding a package to a project’s configuration file *persists for future project sessions and deployments*. This is different than using `conda install` to add a package using the conda environment during a session, which impacts the project *during the current session only*.

<Note>
  Networks that are **air-gapped** (operate without internet access) must [mirror the Anaconda repository into your organization’s internal package repository](../../admin/chan-pkg/mirror) to provide them to users.
</Note>

### Adding conda packages

To add a conda package to your project’s `anaconda-project.yml` file:

1. Open your project.
2. If necessary, start a session.
3. Open a terminal within your session editor.
4. Verify that you are in the `lab_launch` environment.
5. Run the following command:

   <Tabs>
     <Tab title="Add packages command">
       ```sh  theme={null}
       # Replace <PACKAGE_NAME> with the name of the packages you want to add to your project's configuration
       anaconda-project add-packages <PACKAGE_NAME> <PACKAGE_NAME>
       ```
     </Tab>

     <Tab title="From channel">
       ```sh  theme={null}
       # Replace <CHANNEL_NAME> with the name of the channel that contains the packages you want to add
       # Replace <PACKAGE_NAME> with the name of the packages you want to add to your project's configuration
       anaconda-project add-packages --channel <CHANNEL_NAME> <PACKAGE_NAME> <PACKAGE_NAME>
       ```
     </Tab>

     <Tab title="From external repository">
       To use packages from an external repository, you will need to specify the full channel URL in the command:

       ```sh  theme={null}
       # Replace <CHANNEL_URL> with the address of the channel that contains the packages you want to add
       # Replace <PACKAGE_NAME> with the name of the packages you want to add to your project's configuration
       anaconda-project add-packages <PACKAGE_NAME> --channel <CHANNEL_URL>
       ```
     </Tab>
   </Tabs>

   The command may take a moment to run as it solves the environment to collect dependencies and download packages. Once complete, the added packages appear in the project’s `anaconda-project.yml` file. If the file is open when you run the command, close and reopen it to view your changes.
6. [Commit and push your updates to the project](./collaborate#committing-and-pushing-changes).
7. Stop and re-start the project session.

### Adding pip packages

If your project requires you to `pip` install a package, you can use `anaconda-project` to add it to your project’s configuration.

To add a `pip` package to your project’s `anaconda-project.yml` file:

1. Open your project.

2. If necessary, start a session.

3. Open a terminal within your session editor.

4. Verify that you are in the `lab_launch` environment.

5. Run the following command:

   ```sh  theme={null}
    # Replace <PACKAGE_NAME> with the name of the packages you want to add to your project's configuration
    anaconda-project add-packages --pip <PACKAGE_NAME> <PACKAGE_NAME>
   ```

6. [Commit and push your updates to the project](./collaborate#committing-and-pushing-changes).

7. Stop and re-start the project session.

### Removing packages

To remove a package from your project’s `anaconda-project.yml` file:

1. Open your project.

2. If necessary, start a session.

3. Open a terminal within your session editor.

4. Verify that you are in the `lab_launch` environment.

5. Run the following command:

   ```sh  theme={null}
   # Replace <PACKAGE_NAME> with the name of the packages you want to remove from your project's configuration
   anaconda-project remove-packages <PACKAGE_NAME> <PACKAGE_NAME>
   ```

6. [Commit and push your updates to the project](./collaborate#committing-and-pushing-changes).

7. Stop and re-start the project session.

## Configuring project environment variables

Environment variables are key parameters that manage dynamic settings like API keys, database URLs, and memory limits without modifying the codebase. These variables are essential for deploying projects consistently.

To add environment variables with a default value to your project’s `anaconda-project.yml` file:

1. Open your project.

2. If necessary, start a session.

3. Open a terminal within your session editor.

4. Verify that you are in the `lab_launch` environment.

5. Run the following command:

   ```sh  theme={null}
    # Replace <VALUE> with the content of your environment variable
    # Replace <VARIABLE> with the variable name
    anaconda-project add-variable --default=<VALUE> <VARIABLE>
   ```

6. [Commit and push your updates to the project](./collaborate#committing-and-pushing-changes).

7. Stop and re-start the project session.

For more information and advanced command arguments, see [Working with environment variables](https://anaconda-project.readthedocs.io/en/latest/user-guide/tasks/work-with-variables.html) in the official `anaconda-project` documentation.

## Configuring project commands

To deploy a project in Workbench, it must contain at least one appropriate deployment command defined in its `anaconda-project.yml` file. These commands specify how the project’s components, such as notebooks, scripts, or generic web frameworks, should be executed when the project is deployed.

To add a command to your project’s `anaconda-project.yml` file:

1. Open your project.

2. If necessary, start a session.

3. Open a terminal within your session editor.

4. Verify that you are in the `lab_launch` environment.

5. Run the following command:

   ```sh  theme={null}
    # Replace <CMD_NAME> with a name for your deployment command
    # Replace <COMMAND> with the project filename that should be executed
    anaconda-project add-command <CMD_NAME> <COMMAND>
   ```

6. [Commit and push your updates to the project](./collaborate#committing-and-pushing-changes).

7. Stop and re-start the project session.

For more information and advanced command arguments, see [Working with commands](https://anaconda-project.readthedocs.io/en/latest/user-guide/tasks/work-with-commands.html) in the official `anaconda-project` documentation.

<Accordion title="Example deployment commands">
  The following are example deployment commands you can use:

  **For a Notebook:**

  ```yaml  theme={null}
  commands:
  default:
     notebook: <FILE_NAME>.ipynb
  ```

  **For a Panel dashboard**:

  ```yaml  theme={null}
  commands:
  default:
     unix: panel serve <SCRIPT_OR_NOTEBOOK_FILE>
     supports_http_options: True
  ```

  **For a generic script or web framework, including Python or R:**

  ```yaml  theme={null}
  commands:
  default:
     unix: bash <YOUR-SCRIPT>.sh
     supports_http_options: true
  ```

  ```yaml  theme={null}
  commands:
  default:
     unix: python <YOUR-SCRIPT>.py
     supports_http_options: true
  ```

  ```yaml  theme={null}
  commands:
  default:
     unix: Rscript <YOUR-SCRIPT>.R
     supports_http_options: true
  ```
</Accordion>

### Validating project deployment commands

To validate the `anaconda-project.yml` and verify your project will deploy successfully:

1. Open your project.
2. If necessary, start a session.
3. Open a terminal within your session editor.
4. Verify that you are in the `lab_launch` environment.
5. Prepare the environment and test the deployment command by running the following commands:

   ```sh  theme={null}
   # Replace <ENV_NAME> with the name of the project's environment
   # Replace <COMMAND> with the deployment command that you want to test
   anaconda-project prepare --env-spec <ENV_NAME>
   anaconda-project run <COMMAND>
   ```

   Any errors preventing a successful deployment are displayed in the terminal.

### Testing project deployments

Once deployment commands are added to your project, you can test the deployment using the `test_deployment` command. This sets up a mini web application, allowing you to preview your deployment locally using a port within your session.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_deployment_commands_2.png?fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=5974bff6067015438081d7a828b00569" alt="" data-og-width="1922" width="1922" data-og-height="745" height="745" data-path="images/ae5_deployment_commands_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_deployment_commands_2.png?w=280&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=32e36478c9b196b466fd5111fa4be40c 280w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_deployment_commands_2.png?w=560&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=4fd30292316b699bfde4e979e4d117f4 560w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_deployment_commands_2.png?w=840&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=71e3ef35be7617e34c858e3ca2954e62 840w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_deployment_commands_2.png?w=1100&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=0be369364d1d84a424f1e1dd65d6f25b 1100w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_deployment_commands_2.png?w=1650&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=c6541b2f7ae1b09fe32681b3f9e28d33 1650w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_deployment_commands_2.png?w=2500&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=b4407e50096b9e7814ba057015820033 2500w" />
</Frame>

To test a project deployment:

1. Open your project.

2. If necessary, start a session.

3. Open a terminal within your session editor.

4. Verify that you are in the `lab_launch` environment.

5. Test a deployment command you’ve added to your project by running the following command:

   ```sh  theme={null}
    # Replace <COMMAND> with an available deployment command
    test_deployment <COMMAND>
   ```

   <Note>
     If you do not supply a deployment command to test, the first command listed under the `commands:` section of the projects `.yml` configuration file will be run.
   </Note>

6. Navigate to the web address returned by the command to verify your project deployed successfully.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_test_deployment_2.png?fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=e105e1679aa989260235576901109a91" alt="" data-og-width="1922" width="1922" data-og-height="784" height="784" data-path="images/ae5_test_deployment_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_test_deployment_2.png?w=280&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=15d90a8052b87f761a3cd270b5575295 280w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_test_deployment_2.png?w=560&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=a0333e2c1a8ebad83626ad5acb103449 560w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_test_deployment_2.png?w=840&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=b6b1c588e2b5f333a5ce4502f11d0afe 840w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_test_deployment_2.png?w=1100&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=1912c916197422bf3f6cd6630e224ed1 1100w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_test_deployment_2.png?w=1650&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=bc8526dfc789c0e143c84f3b09b0d689 1650w, https://mintcdn.com/anaconda-29683c67/ZgqdN7i1L1qurUKy/images/ae5_test_deployment_2.png?w=2500&fit=max&auto=format&n=ZgqdN7i1L1qurUKy&q=85&s=a5778a637c1080f466e81219c87cdfae 2500w" />
   </Frame>

## Locking project configurations

Project locking is a crucial step in ensuring your project is reproducible across multiple deployments at scale. It is best practice to lock your project once you have finalized configurations for your project, or if you are preparing to transition to a production or public deployment. For more information, see [Project reproducibility in Workbench](../../reference/reproducibility).

To lock your `anaconda-project.yml` file configurations to a fixed state:

1. Open your project.
2. If necessary, start a session.
3. Open a terminal within your session editor.
4. Verify that you are in the `lab_launch` environment.
5. Lock your project configurations by running the following command:

   ```sh  theme={null}
    anaconda-project lock
   ```

This instructs conda to solve the project’s environment, lock all packages and their dependencies to their current versions, and generates an `anaconda-project-lock.yml` file for your project.


# Project logs

Because Data Science & AI Workbench is built on top of a Kubernetes cluster, each project session is created as a pod. Each project session pod has an `editor`, `sync`, and `proxy` container, and logs for each container are accessible to aid you in troubleshooting issues you may encounter with your project. These logs can provide insights to the operational health of your project, possible configuration errors, and potential security issues.

## Viewing project logs

To view a project session’s logs:

1. Log in to Workbench.
2. Open a project.
3. If necessary, start a session in the project.
4. Select <Icon icon="newspaper" iconType="light" /> **Logs** from the left-hand navigation.
5. Open a container dropdown to view the logs for that container.

<Frame>
  <img src="https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_session_logs_2.png?fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=316ce1e50ae8b1bbb94660a5a1099ca5" alt="" data-og-width="1922" width="1922" data-og-height="1001" height="1001" data-path="images/project_session_logs_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_session_logs_2.png?w=280&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=f2af79465b088cc0a34f6ad753731d51 280w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_session_logs_2.png?w=560&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=4554ca6fb81dc00b7ad56177d9b17241 560w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_session_logs_2.png?w=840&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=a87b9aa93620465890003035a7fb2e74 840w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_session_logs_2.png?w=1100&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=57f6c5852df70a0d01be40c0c5a1db79 1100w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_session_logs_2.png?w=1650&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=aab8f1bf04be4ea06f4ef33025fb36b6 1650w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_session_logs_2.png?w=2500&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=55b8a927a01ba4366a6ef9ae1bc87aac 2500w" />
</Frame>

<Tip>
  Use <Icon icon="magnifying-glass" iconType="light" /> **Search** to help you efficiently locate information in the container logs.
</Tip>

### Editor container logs

The editor container is where the integrated development environment (IDE) set by the project configurations runs. Logs from this container can provide insights into the following:

* User actions performed within the editor, such as file edits, saves, and execution of code cells
* Errors or warnings related to the editor software, as opposed to Workbench software
* Problems that are caused by editor plug-ins or extensions

### Sync container logs

The sync container is responsible for synchronizing project files and code between persistent storage and the editor. Logs from this container can provide insights into the following:

* Successes or failures when syncing files between the local user repository and the projects remote repository
* Issues encountered during file creation or deletion, or file modification attempts
* Problems accessing external resources the project relies on

### Proxy container logs

The proxy container handles network traffic to and from the project’s environment, and facilitates access to web interfaces and APIs. Logs from this container can provide insights into the following:

* Incoming and outgoing network requests, which is useful for identifying unauthorized access attempts
* Errors related to network connectivity, DNS issues, or failed attempts to connect to external services
* Information on request handling times and bottlenecks in network communication
# Visualizations and dashboards

Data Science & AI Workbench makes it easy for you to create and share interactive data visualizations, live notebooks or machine learning models built using popular libraries such as Bokeh and HoloViews.

To get you started quickly, Workbench provides sample projects of Bokeh applications for clustering and cross filtering data. There are also several [examples of Workbench projects that use HoloViz here](https://examples.holoviz.org/).

## Create an interactive plot

1. From the <Icon icon="file-code" iconType="light" /> **Projects** view, create a new project using the minimal Python templates:

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_templates_2.png?fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=2216a49d30cd31d1caf9d4fb6030521e" alt="" data-og-width="876" width="876" data-og-height="610" height="610" data-path="images/project_templates_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_templates_2.png?w=280&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=ffbd74f6c8dd78ac783242402a4a38c9 280w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_templates_2.png?w=560&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=af635e0f212d31c657687c1c4c59a58d 560w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_templates_2.png?w=840&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=85e1582f68a0f03408ac48f43324d357 840w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_templates_2.png?w=1100&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=28e9ca099f535b38d95de9719d731735 1100w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_templates_2.png?w=1650&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=e22c691d3306cb0ced56703bc4637901 1650w, https://mintcdn.com/anaconda-29683c67/GAawxvWy-HUVSCqf/images/project_templates_2.png?w=2500&fit=max&auto=format&n=GAawxvWy-HUVSCqf&q=85&s=2c32ee625d14fa0b95a57a89a5b37410 2500w" />
   </Frame>

2. Open a session for your newly created project.

3. Open a terminal.

4. Run the following command to install `hvplot` and `panel`:

   ```
   anaconda-project add-packages hvplot panel
   ```

5. Create a new Notebook and rename it to `tips.ipynb`.

6. Add the following code to `tips.ipynb`:

   ```py  theme={null}
   import pandas as pd
   import hvplot.pandas
   import panel

   panel.extension()

   df = pd.read_csv('http://bit.ly/tips-csv')
   p = df.hvplot.scatter(x='total_bill', y='tip', hover_cols=['sex','day','size'])
   pn.panel(p).servable()

   ```

   <Note>
     In this example, the data is being read from the Internet. Alternatively, you could [download](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv) the `.csv` and upload it to the project.
   </Note>

7. Open the project’s `anaconda-project.yml` file, and add the following deployment command:

   ```yaml  theme={null}
   commands:
     scatter-plot:
     unix: panel serve tips.ipynb
     supports_http_options: True
   ```

8. [Save and commit your changes](./projects/collaborate#committing-and-pushing-changes).

9. [Deploy the project](./deployments/main).

<Tip>
  For a deeper dive into data visualization, follow [this HoloViz tutorial](https://holoviz.org/tutorial/index.html).
</Tip>
# Runtimes

export const AnacondaIcon = () => {
  return <span className="inline_icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" fill="none">
            <path fill="#3AAE2A" fill-rule="evenodd" clip-rule="evenodd" d="M14.9585 0.0451345C14.6119 0.067341 14.3206 0.0931831 14.3113 0.102518C14.302 0.111901 14.5097 0.276485 14.7729 0.468238C15.5956 1.06772 17.2278 2.50068 17.2278 2.62355C17.2278 2.65607 16.9736 2.92069 16.6629 3.21168C16.1371 3.70411 15.2819 4.63801 15.046 4.9772L14.9436 5.12459L15.9511 5.12758C17.7734 5.13294 19.1711 5.44688 20.7258 6.19998C22.9696 7.28688 24.6484 8.95001 25.7693 11.1964C27.8109 15.2883 27.0492 20.3017 23.8861 23.5904C22.9423 24.5717 22.0068 25.2562 20.7845 25.8598C19.2669 26.6092 17.7591 26.9597 16.0439 26.9617C14.31 26.9637 12.8102 26.6203 11.3197 25.8799C10.95 25.6963 10.5828 25.5046 10.5038 25.454C10.3771 25.373 10.3163 25.3675 9.99008 25.4077C9.7866 25.4328 8.97584 25.4558 8.18841 25.4588L6.75671 25.4642L6.7844 25.9064C6.87002 27.2737 7.06165 29.2542 7.11263 29.2986C7.11943 29.3046 7.31214 29.4312 7.54086 29.58C9.41112 30.797 11.7711 31.6382 14.1456 31.9344C14.9341 32.0327 17.3429 32.0174 18.0839 31.9094C21.7606 31.3733 24.775 29.8849 27.3065 27.3557C31.2619 23.4038 32.874 17.6279 31.5394 12.19C30.8534 9.39478 29.5058 6.95609 27.5055 4.8898C25.8492 3.17886 24.01 1.9491 21.8322 1.09646C20.3 0.496586 18.7453 0.156757 17.0084 0.0421376C16.1465 -0.0147053 15.8881 -0.0143614 14.9585 0.0451345ZM10.3784 1.04345C9.13191 1.52143 7.28391 2.49449 7.49203 2.56322C7.53235 2.57653 7.84267 2.64517 8.18166 2.71577C8.5207 2.78632 9.01987 2.90614 9.29096 2.982L9.78391 3.11995L9.98988 2.64841C10.1032 2.38901 10.3374 1.8926 10.5103 1.54521C10.6832 1.19781 10.8178 0.906915 10.8095 0.898809C10.8011 0.890654 10.6072 0.95575 10.3784 1.04345ZM12.2285 1.47672C11.8241 2.2141 11.1791 3.5744 11.2218 3.5999C11.2288 3.60408 11.5869 3.75397 12.0174 3.933C12.4479 4.11198 12.9188 4.30963 13.0637 4.37217L13.3272 4.4859L13.4795 4.29233C13.7576 3.93899 14.3038 3.31087 14.5972 3.00701L14.8867 2.70722L14.455 2.36498C13.6555 1.73121 12.6096 0.973142 12.5346 0.973142C12.5181 0.973142 12.3804 1.19973 12.2285 1.47672ZM6.19604 4.71927C6.16106 5.53492 6.17584 6.93958 6.21992 6.9833C6.23337 6.99662 6.4095 6.98856 6.61131 6.96532C6.81312 6.94208 7.35426 6.90755 7.81385 6.88858L8.64947 6.85414L8.78695 6.28414C8.86253 5.97065 9.00681 5.45425 9.10754 5.13657L9.29071 4.55901L9.03954 4.48649C8.31062 4.27602 6.61493 3.92091 6.3389 3.92091C6.23264 3.92091 6.22961 3.93777 6.19604 4.71927ZM4.32011 5.13446C3.62887 5.8917 2.85534 6.9155 2.47632 7.57468C2.35494 7.78579 2.34981 7.81045 2.43249 7.78441C2.62525 7.72378 3.67148 7.46128 4.22432 7.33487L4.79722 7.2039L4.76796 5.96775C4.75186 5.28784 4.73332 4.72492 4.72672 4.71686C4.72016 4.70875 4.53719 4.89667 4.32011 5.13446ZM10.53 5.52991C10.3635 6.07495 10.1827 6.72611 10.1827 6.78045C10.1827 6.80054 10.2983 6.74822 10.4396 6.66421C10.738 6.48665 11.7 6.00784 12.0908 5.84232L12.3598 5.72839L12.0418 5.58144C11.6811 5.41475 10.7701 5.05089 10.7135 5.05089C10.693 5.05089 10.6104 5.26647 10.53 5.52991ZM7.5164 8.34493C7.11278 8.3637 6.67799 8.38187 6.55015 8.38536C6.33866 8.39111 6.31777 8.40241 6.31777 8.51064C6.31777 8.66245 6.54418 10.0083 6.61278 10.264L6.66468 10.4577L6.99932 9.94788C7.34257 9.42489 7.72638 8.93856 8.12085 8.52681C8.24379 8.39843 8.32325 8.29737 8.29732 8.30214C8.27144 8.30695 7.92002 8.32621 7.5164 8.34493ZM4.16512 8.68441C2.76757 9.00847 1.4478 9.43035 1.48943 9.53971C1.50108 9.57032 1.58019 9.79897 1.66522 10.0478C1.89247 10.7128 2.25411 11.5023 2.70401 12.3153C2.9229 12.7108 3.10504 13.0387 3.10886 13.0439C3.11267 13.0491 3.52266 12.7838 4.01992 12.4544C4.51713 12.1249 5.0844 11.7707 5.28048 11.6673C5.56013 11.5199 5.63112 11.4606 5.60974 11.3929C5.47995 10.9823 5.18269 9.42185 5.11522 8.79702C5.09594 8.61897 5.05901 8.49148 5.02721 8.49359C4.99702 8.49561 4.6091 8.58149 4.16512 8.68441ZM0.788944 11.0211C0.430822 11.9658 0.0928572 13.836 0.0300881 15.2207L0 15.884L0.305137 15.54C0.918592 14.8486 2.09819 13.7591 2.31003 13.6882C2.33988 13.6782 2.24927 13.486 2.10538 13.2541C1.96336 13.0252 1.62158 12.3962 1.34579 11.8563C0.855627 10.8967 0.8432 10.878 0.788944 11.0211ZM5.38763 12.7486C5.18616 12.8712 4.71757 13.1714 4.34638 13.4156L3.67143 13.8596L3.78875 13.9875C3.85328 14.0578 4.07828 14.3474 4.28875 14.6311C4.49922 14.9149 4.77417 15.2686 4.89976 15.4172C5.02535 15.5658 5.1501 15.7282 5.17701 15.778C5.21331 15.8451 5.2343 15.7228 5.25798 15.3064C5.29736 14.6137 5.4482 13.7029 5.63283 13.0424C5.7095 12.7683 5.76811 12.5398 5.76307 12.5347C5.75808 12.5297 5.5891 12.6259 5.38763 12.7486ZM2.30602 14.9957C1.75259 15.4843 0.300147 16.9297 0.300147 16.9919C0.300147 17.0301 1.4932 17.9936 2.01248 18.3747C2.52432 18.7504 3.08645 19.1209 3.10842 19.0973C3.11855 19.0863 3.25294 18.8673 3.40705 18.6106C3.56111 18.3539 3.89452 17.8389 4.14785 17.4662C4.40123 17.0934 4.5933 16.7638 4.57476 16.7336C4.55622 16.7035 4.31874 16.4115 4.04712 16.0848C3.51116 15.4403 3.01903 14.795 2.92569 14.6143C2.86806 14.5028 2.85622 14.51 2.30602 14.9957ZM4.89022 17.9865C4.35798 18.7996 3.96962 19.4516 3.96952 19.5324C3.96943 19.593 6.25045 20.7581 6.29051 20.7178C6.30172 20.7066 6.23621 20.5273 6.14492 20.3194C5.8821 19.7209 5.64081 18.9376 5.50553 18.2439C5.43685 17.8917 5.36586 17.5437 5.34776 17.4706C5.31732 17.3478 5.28269 17.3869 4.89022 17.9865ZM0.0749022 18.1225C0.383758 20.0374 0.755236 21.3555 1.34829 22.6409C1.44819 22.8574 1.47603 22.8874 1.50411 22.8087C1.65798 22.3782 2.15328 21.1704 2.33484 20.7831C2.68063 20.0454 2.75627 19.8389 2.68078 19.8389C2.55778 19.8389 1.04482 18.7691 0.25954 18.1269L0.0477006 17.9537L0.0749022 18.1225ZM3.24374 20.8671C2.89076 21.6228 2.11033 23.6518 2.11033 23.8138C2.11033 23.9473 4.30906 24.3929 5.61596 24.5243L5.86816 24.5496L5.90108 23.9752C5.93049 23.4627 6.01351 22.5993 6.10392 21.8655C6.12926 21.6598 6.12153 21.6075 6.06581 21.6075C5.98499 21.6075 4.64903 20.9528 3.97432 20.5826C3.72138 20.4438 3.50994 20.3302 3.5045 20.3302C3.49903 20.3302 3.38166 20.5718 3.24374 20.8671ZM6.81449 22.3833C6.73748 23.0915 6.64218 24.5536 6.67119 24.5827C6.68396 24.5956 7.29262 24.6002 8.02369 24.5929L9.3529 24.5799L8.86224 24.1478C8.27134 23.6274 7.68743 22.9679 7.28734 22.369C7.12486 22.1259 6.96488 21.9112 6.93181 21.892C6.88719 21.8662 6.85695 21.9927 6.81449 22.3833ZM2.50171 24.827C2.50171 24.898 3.04296 25.671 3.44912 26.1801C3.99961 26.8702 4.6844 27.5869 5.48009 28.3059L6.13748 28.8999L6.10744 28.5085C6.09091 28.2933 6.04482 27.7745 6.00505 27.3557C5.96527 26.9369 5.91806 26.3123 5.90015 25.9678L5.86762 25.3414L5.68905 25.341C5.3389 25.3405 3.43327 25.0159 2.61179 24.817C2.55127 24.8023 2.50171 24.8068 2.50171 24.827Z" />
            </svg>
        </span>;
};

In Anaconda Notebooks, a runtime is what powers your code execution. You can think of a runtime as a conda environment connected to a language-specific kernel. Anaconda Notebooks provides several pre-configured runtimes that include the `ipykernel` package and all the packages from the latest Anaconda Distribution release, giving you immediate access to a comprehensive data science toolkit.

## Environments, kernels, and runtimes

### What is an environment?

An environment is a folder or directory that contains a specific collection of conda packages and their dependencies.

Working in separate environments allows you to maintain and run packages without interference from other collections of packages. For example, you may require separate conda environments to maintain distinct versions of Python based on distinct package dependencies.

### What is a kernel?

A kernel is a programming-language-specific process that interprets your code, runs it, and gives you the results. In Jupyter Notebooks, kernels allow users to run code in cells and receive immediate output. For example, `ipykernel` enables interactive computing in Python.

### What is a runtime?

A runtime in Anaconda Notebooks is a conda environment that has been associated with a specific kernel, enabling it to execute code. For an environment to be usable in JupyterLab, it must contain a kernel package (such as `ipykernel` for Python). Without this kernel association, JupyterLab cannot recognize the environment as an available option for running notebooks.

The default runtimes provided in Anaconda Notebooks come with the `ipykernel` package already installed, making them immediately available for your Python notebooks.

To add a kernel package to a custom environment and create your own runtime, see [creating custom runtimes](#creating-custom-runtimes).

## Using default runtimes

Custom runtimes often use large amounts of your limited Anaconda Notebooks storage space. Because of this, Anaconda provides a number of *read-only* default runtimes that contain all the packages from the latest release of Anaconda Distribution.

The default runtime naming convention is typically `anaconda-<YEAR>.<MONTH>-py<PYTHON_VERSION>`, which maps to Anaconda Distribution releases:

| Environment Name         | Status | Description                                                                                         |
| :----------------------- | :----- | :-------------------------------------------------------------------------------------------------- |
| anaconda-2024.02-py10    | Live   | Latest Anaconda Packages (stable & recommended)                                                     |
| anaconda-ai-2024.04-py10 | Live   | Latest Anaconda Packages + AI Packages                                                              |
| anaconda-01-nvidia-a10   | Live   | Latest Anaconda, AI, + NVIDIA Packages (see [GPU Runtimes](/tools/anaconda-notebooks/gpu-runtimes)) |

<AccordionGroup>
  <Accordion title="Packages included in anaconda-2024.02-py10">
    | Package Name               | Package Version |
    | :------------------------- | :-------------- |
    | \_anaconda\_depends        | 2024.02         |
    | \_libgcc\_mutex            | 0.1             |
    | \_openmp\_mutex            | 5.1             |
    | abseil-cpp                 | 20211102        |
    | aiobotocore                | 2.7.0           |
    | aiohttp                    | 3.9.3           |
    | aioitertools               | 0.7.1           |
    | aiosignal                  | 1.2.0           |
    | alabaster                  | 0.7.12          |
    | altair                     | 5.0.1           |
    | anaconda-catalogs          | 0.2.0           |
    | anyio                      | 4.2.0           |
    | aom                        | 3.6.0           |
    | appdirs                    | 1.4.4           |
    | argon2-cffi                | 21.3.0          |
    | argon2-cffi-bindings       | 21.2.0          |
    | arrow                      | 1.2.3           |
    | arrow-cpp                  | 14.0.2          |
    | astroid                    | 2.14.2          |
    | astropy                    | 5.3.4           |
    | asttokens                  | 2.0.5           |
    | async-lru                  | 2.0.4           |
    | async-timeout              | 4.0.3           |
    | atomicwrites               | 1.4.0           |
    | attrs                      | 23.1.0          |
    | automat                    | 20.2.0          |
    | autopep8                   | 2.0.4           |
    | aws-c-auth                 | 0.6.19          |
    | aws-c-cal                  | 0.5.20          |
    | aws-c-common               | 0.8.5           |
    | aws-c-compression          | 0.2.16          |
    | aws-c-event-stream         | 0.2.15          |
    | aws-c-http                 | 0.6.25          |
    | aws-c-io                   | 0.13.10         |
    | aws-c-mqtt                 | 0.7.13          |
    | aws-c-s3                   | 0.1.51          |
    | aws-c-sdkutils             | 0.1.6           |
    | aws-checksums              | 0.1.13          |
    | aws-crt-cpp                | 0.18.16         |
    | aws-sdk-cpp                | 1.10.55         |
    | babel                      | 2.11.0          |
    | bcrypt                     | 3.2.0           |
    | beautifulsoup4             | 4.12.2          |
    | binaryornot                | 0.4.4           |
    | black                      | 24.3.0          |
    | blas                       | 1               |
    | bleach                     | 4.1.0           |
    | blinker                    | 1.6.2           |
    | blosc                      | 1.21.3          |
    | bokeh                      | 3.4.0           |
    | boost-cpp                  | 1.82.0          |
    | botocore                   | 1.31.64         |
    | bottleneck                 | 1.3.7           |
    | brotli                     | 1.0.9           |
    | brotli-bin                 | 1.0.9           |
    | brotli-python              | 1.0.9           |
    | brunsli                    | 0.1             |
    | bzip2                      | 1.0.8           |
    | c-ares                     | 1.19.1          |
    | c-blosc2                   | 2.12.0          |
    | ca-certificates            | 2024.3.11       |
    | cachetools                 | 4.2.2           |
    | certifi                    | 2024.2.2        |
    | cffi                       | 1.16.0          |
    | cfgv                       | 3.4.0           |
    | cfitsio                    | 3.47            |
    | chardet                    | 4.0.0           |
    | charls                     | 2.2.0           |
    | charset-normalizer         | 2.0.4           |
    | click                      | 8.1.7           |
    | cloudpickle                | 2.2.1           |
    | colorama                   | 0.4.6           |
    | colorcet                   | 3.1.0           |
    | comm                       | 0.2.1           |
    | constantly                 | 23.10.4         |
    | contourpy                  | 1.2.0           |
    | cookiecutter               | 2.6.0           |
    | cryptography               | 42.0.5          |
    | cssselect                  | 1.2.0           |
    | curl                       | 8.5.0           |
    | cycler                     | 0.11.0          |
    | cyrus-sasl                 | 2.1.28          |
    | cytoolz                    | 0.12.2          |
    | dask                       | 2023.11.0       |
    | dask-core                  | 2023.11.0       |
    | datashader                 | 0.16.0          |
    | dav1d                      | 1.2.1           |
    | dbus                       | 1.13.18         |
    | debugpy                    | 1.6.7           |
    | decorator                  | 5.1.1           |
    | defusedxml                 | 0.7.1           |
    | diff-match-patch           | 20200713        |
    | dill                       | 0.3.7           |
    | distlib                    | 0.3.6           |
    | distributed                | 2023.11.0       |
    | docstring-to-markdown      | 0.11            |
    | docutils                   | 0.18.1          |
    | entrypoints                | 0.4             |
    | et\_xmlfile                | 1.1.0           |
    | exceptiongroup             | 1.2.0           |
    | executing                  | 0.8.3           |
    | expat                      | 2.5.0           |
    | filelock                   | 3.13.1          |
    | flake8                     | 6.0.0           |
    | flask                      | 2.2.5           |
    | fontconfig                 | 2.14.1          |
    | fonttools                  | 4.25.0          |
    | freetype                   | 2.12.1          |
    | frozenlist                 | 1.4.0           |
    | fsspec                     | 2023.10.0       |
    | gensim                     | 4.3.0           |
    | gflags                     | 2.2.2           |
    | giflib                     | 5.2.1           |
    | gitdb                      | 4.0.7           |
    | gitpython                  | 3.1.37          |
    | glib                       | 2.78.4          |
    | glib-tools                 | 2.78.4          |
    | glog                       | 0.5.0           |
    | gmp                        | 6.2.1           |
    | gmpy2                      | 2.1.2           |
    | greenlet                   | 3.0.1           |
    | grpc-cpp                   | 1.48.2          |
    | gst-plugins-base           | 1.14.1          |
    | gstreamer                  | 1.14.1          |
    | h5py                       | 3.9.0           |
    | hdf5                       | 1.12.1          |
    | heapdict                   | 1.0.1           |
    | holoviews                  | 1.18.3          |
    | hvplot                     | 0.9.2           |
    | hyperlink                  | 21.0.0          |
    | icu                        | 73.1            |
    | identify                   | 2.5.5           |
    | idna                       | 3.4             |
    | imagecodecs                | 2023.1.23       |
    | imageio                    | 2.33.1          |
    | imagesize                  | 1.4.1           |
    | imbalanced-learn           | 0.11.0          |
    | importlib-metadata         | 7.0.1           |
    | importlib\_metadata        | 7.0.1           |
    | incremental                | 22.10.0         |
    | inflection                 | 0.5.1           |
    | iniconfig                  | 1.1.1           |
    | intake                     | 0.6.8           |
    | intel-openmp               | 2023.1.0        |
    | intervaltree               | 3.1.0           |
    | ipykernel                  | 6.28.0          |
    | ipython                    | 8.20.0          |
    | ipython\_genutils          | 0.2.0           |
    | ipywidgets                 | 8.1.2           |
    | isort                      | 5.9.3           |
    | itemadapter                | 0.3.0           |
    | itemloaders                | 1.1.0           |
    | itsdangerous               | 2.0.1           |
    | jaraco.classes             | 3.2.1           |
    | jedi                       | 0.18.1          |
    | jeepney                    | 0.7.1           |
    | jellyfish                  | 1.0.1           |
    | jinja2                     | 3.1.3           |
    | jmespath                   | 1.0.1           |
    | joblib                     | 1.2.0           |
    | jpeg                       | 9e              |
    | jq                         | 1.6             |
    | json5                      | 0.9.6           |
    | jsonschema                 | 4.19.2          |
    | jsonschema-specifications  | 2023.7.1        |
    | jupyter                    | 1.0.0           |
    | jupyter-lsp                | 2.2.0           |
    | jupyter\_client            | 8.6.0           |
    | jupyter\_console           | 6.6.3           |
    | jupyter\_core              | 5.5.0           |
    | jupyter\_events            | 0.8.0           |
    | jupyter\_server            | 2.10.0          |
    | jupyter\_server\_terminals | 0.4.4           |
    | jupyterlab                 | 4.0.11          |
    | jupyterlab-variableinspect | or 3.1.0        |
    | jupyterlab\_pygments       | 0.1.2           |
    | jupyterlab\_server         | 2.25.1          |
    | jupyterlab\_widgets        | 3.0.10          |
    | jxrlib                     | 1.1             |
    | keyring                    | 24.3.1          |
    | kiwisolver                 | 1.4.4           |
    | krb5                       | 1.20.1          |
    | lazy-object-proxy          | 1.6.0           |
    | lazy\_loader               | 0.3             |
    | lcms2                      | 2.12            |
    | ld\_impl\_linux-64         | 2.38            |
    | lerc                       | 3               |
    | libaec                     | 1.0.4           |
    | libavif                    | 0.11.1          |
    | libboost                   | 1.82.0          |
    | libbrotlicommon            | 1.0.9           |
    | libbrotlidec               | 1.0.9           |
    | libbrotlienc               | 1.0.9           |
    | libclang                   | 14.0.6          |
    | libclang13                 | 14.0.6          |
    | libcups                    | 2.4.2           |
    | libcurl                    | 8.5.0           |
    | libdeflate                 | 1.17            |
    | libedit                    | 3.1.20230828    |
    | libev                      | 4.33            |
    | libevent                   | 2.1.12          |
    | libffi                     | 3.4.4           |
    | libgcc-ng                  | 11.2.0          |
    | libgfortran-ng             | 11.2.0          |
    | libgfortran5               | 11.2.0          |
    | libglib                    | 2.78.4          |
    | libgomp                    | 11.2.0          |
    | libiconv                   | 1.16            |
    | libllvm14                  | 14.0.6          |
    | libnghttp2                 | 1.57.0          |
    | libpng                     | 1.6.39          |
    | libpq                      | 12.17           |
    | libprotobuf                | 3.20.3          |
    | libsodium                  | 1.0.18          |
    | libspatialindex            | 1.9.3           |
    | libssh2                    | 1.10.0          |
    | libstdcxx-ng               | 11.2.0          |
    | libthrift                  | 0.15.0          |
    | libtiff                    | 4.5.1           |
    | libuuid                    | 1.41.5          |
    | libwebp-base               | 1.3.2           |
    | libxcb                     | 1.15            |
    | libxkbcommon               | 1.0.1           |
    | libxml2                    | 2.10.4          |
    | libxslt                    | 1.1.37          |
    | libzopfli                  | 1.0.3           |
    | linkify-it-py              | 2.0.0           |
    | llvmlite                   | 0.42.0          |
    | locket                     | 1.0.0           |
    | lxml                       | 4.9.3           |
    | lz4                        | 4.3.2           |
    | lz4-c                      | 1.9.4           |
    | lzo                        | 2.1             |
    | markdown                   | 3.4.1           |
    | markdown-it-py             | 2.2.0           |
    | markupsafe                 | 2.1.3           |
    | matplotlib                 | 3.8.0           |
    | matplotlib-base            | 3.8.0           |
    | matplotlib-inline          | 0.1.6           |
    | mccabe                     | 0.7.0           |
    | mdit-py-plugins            | 0.3.0           |
    | mdurl                      | 0.1.0           |
    | mistune                    | 2.0.4           |
    | mkl                        | 2023.1.0        |
    | mkl-service                | 2.4.0           |
    | mkl\_fft                   | 1.3.8           |
    | mkl\_random                | 1.2.4           |
    | more-itertools             | 10.1.0          |
    | mpc                        | 1.1.0           |
    | mpfr                       | 4.0.2           |
    | mpmath                     | 1.3.0           |
    | msgpack-python             | 1.0.3           |
    | multidict                  | 6.0.4           |
    | multipledispatch           | 0.6.0           |
    | munkres                    | 1.1.4           |
    | mypy                       | 1.8.0           |
    | mypy\_extensions           | 1.0.0           |
    | mysql                      | 5.7.24          |
    | nbclient                   | 0.8.0           |
    | nbconvert                  | 7.10.0          |
    | nbformat                   | 5.9.2           |
    | ncurses                    | 6.4             |
    | nest-asyncio               | 1.6.0           |
    | networkx                   | 3.1             |
    | nltk                       | 3.8.1           |
    | nodeenv                    | 1.7.0           |
    | notebook                   | 7.0.8           |
    | notebook-shim              | 0.2.3           |
    | nspr                       | 4.35            |
    | nss                        | 3.89.1          |
    | numba                      | 0.59.1          |
    | numexpr                    | 2.8.7           |
    | numpy                      | 1.26.4          |
    | numpy-base                 | 1.26.4          |
    | numpydoc                   | 1.5.0           |
    | oniguruma                  | 6.9.7.1         |
    | openjpeg                   | 2.4.0           |
    | openpyxl                   | 3.0.10          |
    | openssl                    | 3.0.13          |
    | orc                        | 1.7.4           |
    | overrides                  | 7.4.0           |
    | packaging                  | 23.2            |
    | pandas                     | 2.1.4           |
    | pandocfilters              | 1.5.0           |
    | panel                      | 1.4.1           |
    | param                      | 2.1.0           |
    | parsel                     | 1.8.1           |
    | parso                      | 0.8.3           |
    | partd                      | 1.4.1           |
    | pathspec                   | 0.10.3          |
    | patsy                      | 0.5.3           |
    | pcre2                      | 10.42           |
    | pexpect                    | 4.8.0           |
    | pickleshare                | 0.7.5           |
    | pillow                     | 10.2.0          |
    | pip                        | 23.3.1          |
    | platformdirs               | 2.5.2           |
    | plotly                     | 5.19.0          |
    | pluggy                     | 1.0.0           |
    | ply                        | 3.11            |
    | pre-commit                 | 3.4.0           |
    | prometheus\_client         | 0.14.1          |
    | prompt-toolkit             | 3.0.43          |
    | prompt\_toolkit            | 3.0.43          |
    | protego                    | 0.1.16          |
    | protobuf                   | 3.20.3          |
    | psutil                     | 5.9.0           |
    | ptyprocess                 | 0.7.0           |
    | pure\_eval                 | 0.2.2           |
    | py-cpuinfo                 | 9.0.0           |
    | pyarrow                    | 14.0.2          |
    | pyasn1                     | 0.4.8           |
    | pyasn1-modules             | 0.2.8           |
    | pycodestyle                | 2.10.0          |
    | pycparser                  | 2.21            |
    | pyct                       | 0.5.0           |
    | pycurl                     | 7.45.2          |
    | pydeck                     | 0.7.1           |
    | pydispatcher               | 2.0.5           |
    | pydocstyle                 | 6.3.0           |
    | pyerfa                     | 2.0.0           |
    | pyflakes                   | 3.0.1           |
    | pygments                   | 2.15.1          |
    | pylint                     | 2.16.2          |
    | pylint-venv                | 3.0.3           |
    | pyls-spyder                | 0.4.0           |
    | pympler                    | 0.9             |
    | pyodbc                     | 5.0.1           |
    | pyopenssl                  | 24.0.0          |
    | pyparsing                  | 3.0.9           |
    | pyqt                       | 5.15.10         |
    | pyqt5-sip                  | 12.13.0         |
    | pyqtwebengine              | 5.15.10         |
    | pysocks                    | 1.7.1           |
    | pytables                   | 3.9.2           |
    | pytest                     | 7.4.0           |
    | python                     | 3.10.14         |
    | python-dateutil            | 2.8.2           |
    | python-fastjsonschema      | 2.16.2          |
    | python-json-logger         | 2.0.7           |
    | python-lmdb                | 1.4.1           |
    | python-lsp-black           | 2.0.0           |
    | python-lsp-jsonrpc         | 1.1.2           |
    | python-lsp-server          | 1.7.2           |
    | python-slugify             | 5.0.2           |
    | python-snappy              | 0.6.1           |
    | python-tzdata              | 2023.3          |
    | pytoolconfig               | 1.2.6           |
    | pytz                       | 2023.3.post1    |
    | pyviz\_comms               | 3.0.2           |
    | pywavelets                 | 1.5.0           |
    | pyxdg                      | 0.27            |
    | pyyaml                     | 6.0.1           |
    | pyzmq                      | 25.1.2          |
    | qdarkstyle                 | 3.0.2           |
    | qstylizer                  | 0.2.2           |
    | qt-main                    | 5.15.2          |
    | qt-webengine               | 5.15.9          |
    | qtawesome                  | 1.2.2           |
    | qtconsole                  | 5.4.2           |
    | qtpy                       | 2.4.1           |
    | queuelib                   | 1.6.2           |
    | re2                        | 2022.04.01      |
    | readline                   | 8.2             |
    | referencing                | 0.30.2          |
    | regex                      | 2023.10.3       |
    | requests                   | 2.31.0          |
    | requests-file              | 1.5.1           |
    | rfc3339-validator          | 0.1.4           |
    | rfc3986-validator          | 0.1.1           |
    | rich                       | 13.3.5          |
    | rope                       | 1.12.0          |
    | rpds-py                    | 0.10.6          |
    | rtree                      | 1.0.1           |
    | s2n                        | 1.3.27          |
    | s3fs                       | 2023.10.0       |
    | scikit-image               | 0.22.0          |
    | scikit-learn               | 1.3.0           |
    | scipy                      | 1.12.0          |
    | scrapy                     | 2.11.1          |
    | seaborn                    | 0.12.2          |
    | secretstorage              | 3.3.1           |
    | semver                     | 3.0.2           |
    | send2trash                 | 1.8.2           |
    | service\_identity          | 18.1.0          |
    | setuptools                 | 68.2.2          |
    | sip                        | 6.7.12          |
    | six                        | 1.16.0          |
    | smart\_open                | 5.2.1           |
    | smmap                      | 4.0.0           |
    | snappy                     | 1.1.10          |
    | sniffio                    | 1.3.0           |
    | snowballstemmer            | 2.2.0           |
    | sortedcontainers           | 2.4.0           |
    | soupsieve                  | 2.5             |
    | sphinx                     | 5.0.2           |
    | sphinxcontrib-applehelp    | 1.0.2           |
    | sphinxcontrib-devhelp      | 1.0.2           |
    | sphinxcontrib-htmlhelp     | 2.0.0           |
    | sphinxcontrib-jsmath       | 1.0.1           |
    | sphinxcontrib-qthelp       | 1.0.3           |
    | sphinxcontrib-serializingh | tml 1.1.5       |
    | spyder                     | 5.4.3           |
    | spyder-kernels             | 2.4.4           |
    | sqlalchemy                 | 2.0.25          |
    | sqlite                     | 3.41.2          |
    | stack\_data                | 0.2.0           |
    | statsmodels                | 0.14.0          |
    | streamlit                  | 1.16.0          |
    | sympy                      | 1.12            |
    | tabulate                   | 0.9.0           |
    | tbb                        | 2021.8.0        |
    | tblib                      | 1.7.0           |
    | tenacity                   | 8.2.2           |
    | terminado                  | 0.17.1          |
    | text-unidecode             | 1.3             |
    | textdistance               | 4.2.1           |
    | threadpoolctl              | 2.2.0           |
    | three-merge                | 0.1.1           |
    | tifffile                   | 2023.4.12       |
    | tinycss2                   | 1.2.1           |
    | tk                         | 8.6.12          |
    | tldextract                 | 3.2.0           |
    | toml                       | 0.10.2          |
    | tomli                      | 2.0.1           |
    | tomlkit                    | 0.11.1          |
    | toolz                      | 0.12.0          |
    | tornado                    | 6.3.3           |
    | tqdm                       | 4.65.0          |
    | traitlets                  | 5.7.1           |
    | twisted                    | 23.10.0         |
    | typing-extensions          | 4.9.0           |
    | typing\_extensions         | 4.9.0           |
    | tzdata                     | 2024a           |
    | tzlocal                    | 2.1             |
    | uc-micro-py                | 1.0.1           |
    | ujson                      | 5.4.0           |
    | ukkonen                    | 1.0.1           |
    | unidecode                  | 1.2.0           |
    | unixodbc                   | 2.3.11          |
    | urllib3                    | 2.0.7           |
    | utf8proc                   | 2.6.1           |
    | validators                 | 0.18.2          |
    | virtualenv                 | 20.17.1         |
    | w3lib                      | 2.1.2           |
    | watchdog                   | 2.1.6           |
    | wcwidth                    | 0.2.5           |
    | webencodings               | 0.5.1           |
    | websocket-client           | 0.58.0          |
    | werkzeug                   | 2.2.3           |
    | whatthepatch               | 1.0.2           |
    | wheel                      | 0.41.2          |
    | widgetsnbextension         | 4.0.10          |
    | wrapt                      | 1.14.1          |
    | wurlitzer                  | 3.0.2           |
    | xarray                     | 2023.6.0        |
    | xyzservices                | 2022.9.0        |
    | xz                         | 5.4.6           |
    | yaml                       | 0.2.5           |
    | yapf                       | 0.31.0          |
    | yarl                       | 1.9.3           |
    | zeromq                     | 4.3.5           |
    | zfp                        | 1.0.0           |
    | zict                       | 3.0.0           |
    | zipp                       | 3.17.0          |
    | zlib                       | 1.2.13          |
    | zlib-ng                    | 2.0.7           |
    | zope                       | 1               |
    | zope.interface             | 5.4.0           |
    | zstd                       | 1.5.5           |
  </Accordion>

  <Accordion title="Packages included in anaconda-ai-2024.04-py10">
    | Package Name               | Package Version |
    | :------------------------- | :-------------- |
    | \_anaconda\_depends        | 2024.02         |
    | \_libgcc\_mutex            | 0.1             |
    | \_openmp\_mutex            | 5.1             |
    | \_py-xgboost-mutex         | 2               |
    | \_tflow\_select            | 2.3.0           |
    | abseil-cpp                 | 20211102        |
    | absl-py                    | 1.4.0           |
    | aiobotocore                | 2.7.0           |
    | aiohttp                    | 3.9.3           |
    | aioitertools               | 0.7.1           |
    | aiosignal                  | 1.2.0           |
    | alabaster                  | 0.7.12          |
    | altair                     | 5.0.1           |
    | anaconda-catalogs          | 0.2.0           |
    | annotated-types            | 0.6.0           |
    | anyio                      | 4.2.0           |
    | aom                        | 3.6.0           |
    | appdirs                    | 1.4.4           |
    | argon2-cffi                | 21.3.0          |
    | argon2-cffi-bindings       | 21.2.0          |
    | arrow                      | 1.2.3           |
    | arrow-cpp                  | 11.0.0          |
    | astroid                    | 2.14.2          |
    | astropy                    | 5.3.4           |
    | asttokens                  | 2.0.5           |
    | astunparse                 | 1.6.3           |
    | async-lru                  | 2.0.4           |
    | async-timeout              | 4.0.3           |
    | atomicwrites               | 1.4.0           |
    | attrs                      | 23.1.0          |
    | automat                    | 20.2.0          |
    | autopep8                   | 2.0.4           |
    | aws-c-common               | 0.4.57          |
    | aws-c-event-stream         | 0.1.6           |
    | aws-checksums              | 0.1.9           |
    | aws-sdk-cpp                | 1.8.185         |
    | babel                      | 2.11.0          |
    | backoff                    | 2.2.1           |
    | bcrypt                     | 4.1.2           |
    | beautifulsoup4             | 4.12.2          |
    | binaryornot                | 0.4.4           |
    | black                      | 24.3.0          |
    | blas                       | 1               |
    | bleach                     | 4.1.0           |
    | blinker                    | 1.6.2           |
    | blosc                      | 1.21.3          |
    | bokeh                      | 3.4.0           |
    | boost-cpp                  | 1.73.0          |
    | botocore                   | 1.31.64         |
    | bottleneck                 | 1.3.7           |
    | brotli                     | 1.0.9           |
    | brotli-bin                 | 1.0.9           |
    | brotli-python              | 1.0.9           |
    | brunsli                    | 0.1             |
    | bzip2                      | 1.0.8           |
    | c-ares                     | 1.19.1          |
    | c-blosc2                   | 2.12.0          |
    | ca-certificates            | 2024.3.11       |
    | cachetools                 | 4.2.2           |
    | cairo                      | 1.16.0          |
    | catalogue                  | 2.0.10          |
    | certifi                    | 2024.2.2        |
    | cffi                       | 1.16.0          |
    | cfgv                       | 3.4.0           |
    | cfitsio                    | 3.47            |
    | chardet                    | 4.0.0           |
    | charls                     | 2.2.0           |
    | charset-normalizer         | 2.0.4           |
    | chroma-hnswlib             | 0.7.3           |
    | chromadb                   | 0.4.17          |
    | click                      | 8.1.7           |
    | cloudpathlib               | 0.16.0          |
    | cloudpickle                | 2.2.1           |
    | colorama                   | 0.4.6           |
    | colorcet                   | 3.1.0           |
    | coloredlogs                | 15.0.1          |
    | comm                       | 0.2.1           |
    | confection                 | 0.1.4           |
    | constantly                 | 23.10.4         |
    | contourpy                  | 1.2.0           |
    | cookiecutter               | 2.6.0           |
    | cryptography               | 41.0.3          |
    | cssselect                  | 1.2.0           |
    | ctransformers              | 0.2.27          |
    | curl                       | 8.2.1           |
    | cycler                     | 0.11.0          |
    | cymem                      | 2.0.6           |
    | cyrus-sasl                 | 2.1.28          |
    | cython-blis                | 0.7.9           |
    | cytoolz                    | 0.12.2          |
    | dask                       | 2023.11.0       |
    | dask-core                  | 2023.11.0       |
    | dataclasses-json           | 0.6.4           |
    | datasets                   | 2.12.0          |
    | datashader                 | 0.16.0          |
    | dav1d                      | 1.2.1           |
    | dbus                       | 1.13.18         |
    | debugpy                    | 1.6.7           |
    | decorator                  | 5.1.1           |
    | defusedxml                 | 0.7.1           |
    | deprecated                 | 1.2.14          |
    | diff-match-patch           | 20200713        |
    | dill                       | 0.3.6           |
    | dirtyjson                  | 1.0.8           |
    | distlib                    | 0.3.6           |
    | distributed                | 2023.11.0       |
    | distro                     | 1.9.0           |
    | docstring-to-markdown      | 0.11            |
    | docutils                   | 0.18.1          |
    | eigen                      | 3.4.0           |
    | entrypoints                | 0.4             |
    | et\_xmlfile                | 1.1.0           |
    | exceptiongroup             | 1.2.0           |
    | executing                  | 0.8.3           |
    | expat                      | 2.5.0           |
    | fastapi                    | 0.110.1         |
    | ffmpeg                     | 4.2.2           |
    | filelock                   | 3.13.1          |
    | flake8                     | 6.0.0           |
    | flask                      | 2.2.5           |
    | flatbuffers                | 2.0.0           |
    | fontconfig                 | 2.14.1          |
    | fonttools                  | 4.25.0          |
    | freetype                   | 2.12.1          |
    | frozenlist                 | 1.4.0           |
    | fsspec                     | 2023.10.0       |
    | gast                       | 0.4.0           |
    | gensim                     | 4.3.0           |
    | gflags                     | 2.2.2           |
    | giflib                     | 5.2.1           |
    | gitdb                      | 4.0.7           |
    | gitpython                  | 3.1.37          |
    | glib                       | 2.78.4          |
    | glib-tools                 | 2.78.4          |
    | glog                       | 0.5.0           |
    | gmp                        | 6.2.1           |
    | gmpy2                      | 2.1.2           |
    | gnutls                     | 3.6.15          |
    | google-auth                | 2.6.0           |
    | google-auth-oauthlib       | 0.4.4           |
    | google-pasta               | 0.2.0           |
    | googleapis-common-protos   | 1.63.0          |
    | graphite2                  | 1.3.14          |
    | greenlet                   | 3.0.1           |
    | grpc-cpp                   | 1.46.1          |
    | grpcio                     | 1.62.1          |
    | gst-plugins-base           | 1.14.1          |
    | gstreamer                  | 1.14.1          |
    | h11                        | 0.14.0          |
    | h5py                       | 3.9.0           |
    | harfbuzz                   | 4.3.0           |
    | hdf5                       | 1.12.1          |
    | heapdict                   | 1.0.1           |
    | holoviews                  | 1.18.3          |
    | httpcore                   | 1.0.2           |
    | httptools                  | 0.6.1           |
    | httpx                      | 0.26.0          |
    | huggingface\_accelerate    | 0.21.0          |
    | huggingface\_hub           | 0.20.3          |
    | humanfriendly              | 10              |
    | hvplot                     | 0.9.2           |
    | hyperlink                  | 21.0.0          |
    | icu                        | 58.2            |
    | identify                   | 2.5.5           |
    | idna                       | 3.4             |
    | imagecodecs                | 2023.1.23       |
    | imageio                    | 2.33.1          |
    | imagesize                  | 1.4.1           |
    | imbalanced-learn           | 0.11.0          |
    | importlib-metadata         | 7.0.1           |
    | importlib-resources        | 6.4.0           |
    | importlib\_metadata        | 7.0.1           |
    | incremental                | 22.10.0         |
    | inflection                 | 0.5.1           |
    | iniconfig                  | 1.1.1           |
    | intake                     | 0.6.8           |
    | intel-openmp               | 2023.1.0        |
    | intervaltree               | 3.1.0           |
    | ipykernel                  | 6.28.0          |
    | ipython                    | 8.20.0          |
    | ipython\_genutils          | 0.2.0           |
    | ipywidgets                 | 8.1.2           |
    | isort                      | 5.9.3           |
    | itemadapter                | 0.3.0           |
    | itemloaders                | 1.1.0           |
    | itsdangerous               | 2.0.1           |
    | jaraco.classes             | 3.2.1           |
    | jedi                       | 0.18.1          |
    | jeepney                    | 0.7.1           |
    | jellyfish                  | 1.0.1           |
    | jinja2                     | 3.1.3           |
    | jmespath                   | 1.0.1           |
    | joblib                     | 1.2.0           |
    | jpeg                       | 9e              |
    | jq                         | 1.6             |
    | json5                      | 0.9.6           |
    | jsonpatch                  | 1.33            |
    | jsonpointer                | 2.4             |
    | jsonschema                 | 4.19.2          |
    | jsonschema-specifications  | 2023.7.1        |
    | jupyter                    | 1.0.0           |
    | jupyter-lsp                | 2.2.0           |
    | jupyter\_client            | 8.6.0           |
    | jupyter\_console           | 6.6.3           |
    | jupyter\_core              | 5.5.0           |
    | jupyter\_events            | 0.8.0           |
    | jupyter\_server            | 2.10.0          |
    | jupyter\_server\_terminals | 0.4.4           |
    | jupyterlab                 | 4.0.11          |
    | jupyterlab-variableinspect | or 3.1.0        |
    | jupyterlab\_pygments       | 0.1.2           |
    | jupyterlab\_server         | 2.25.1          |
    | jupyterlab\_widgets        | 3.0.10          |
    | jxrlib                     | 1.1             |
    | keras                      | 2.11.0          |
    | keras-preprocessing        | 1.1.2           |
    | keyring                    | 24.3.1          |
    | kiwisolver                 | 1.4.4           |
    | krb5                       | 1.20.1          |
    | kubernetes                 | 29.0.0          |
    | lame                       | 3.1             |
    | langchain                  | 0.1.16          |
    | langchain-community        | 0.0.32          |
    | langchain-core             | 0.1.42          |
    | langchain-text-splitters   | 0.0.1           |
    | langcodes                  | 3.3.0           |
    | langsmith                  | 0.1.45          |
    | lazy-object-proxy          | 1.6.0           |
    | lazy\_loader               | 0.3             |
    | lcms2                      | 2.12            |
    | ld\_impl\_linux-64         | 2.38            |
    | lerc                       | 3               |
    | libaec                     | 1.0.4           |
    | libavif                    | 0.11.1          |
    | libboost                   | 1.73.0          |
    | libbrotlicommon            | 1.0.9           |
    | libbrotlidec               | 1.0.9           |
    | libbrotlienc               | 1.0.9           |
    | libclang                   | 14.0.6          |
    | libclang13                 | 14.0.6          |
    | libcups                    | 2.4.2           |
    | libcurl                    | 8.2.1           |
    | libdeflate                 | 1.17            |
    | libedit                    | 3.1.20230828    |
    | libev                      | 4.33            |
    | libevent                   | 2.1.12          |
    | libffi                     | 3.4.4           |
    | libgcc-ng                  | 11.2.0          |
    | libgfortran-ng             | 11.2.0          |
    | libgfortran5               | 11.2.0          |
    | libglib                    | 2.78.4          |
    | libgomp                    | 11.2.0          |
    | libiconv                   | 1.16            |
    | libidn2                    | 2.3.4           |
    | libllvm14                  | 14.0.6          |
    | libnghttp2                 | 1.52.0          |
    | libopenblas                | 0.3.21          |
    | libopus                    | 1.3.1           |
    | libpng                     | 1.6.39          |
    | libpq                      | 12.15           |
    | libprotobuf                | 3.20.3          |
    | libsodium                  | 1.0.18          |
    | libspatialindex            | 1.9.3           |
    | libssh2                    | 1.10.0          |
    | libstdcxx-ng               | 11.2.0          |
    | libtasn1                   | 4.19.0          |
    | libthrift                  | 0.15.0          |
    | libtiff                    | 4.5.1           |
    | libunistring               | 0.9.10          |
    | libuuid                    | 1.41.5          |
    | libvpx                     | 1.7.0           |
    | libwebp                    | 1.3.2           |
    | libwebp-base               | 1.3.2           |
    | libxcb                     | 1.15            |
    | libxgboost                 | 1.7.6           |
    | libxkbcommon               | 1.0.1           |
    | libxml2                    | 2.10.4          |
    | libxslt                    | 1.1.37          |
    | libzopfli                  | 1.0.3           |
    | linkify-it-py              | 2.0.0           |
    | llama-index                | 0.9.48          |
    | llvmlite                   | 0.42.0          |
    | locket                     | 1.0.0           |
    | lxml                       | 4.9.3           |
    | lz4                        | 4.3.2           |
    | lz4-c                      | 1.9.4           |
    | lzo                        | 2.1             |
    | markdown                   | 3.4.1           |
    | markdown-it-py             | 2.2.0           |
    | markupsafe                 | 2.1.3           |
    | marshmallow                | 3.21.1          |
    | matplotlib                 | 3.8.0           |
    | matplotlib-base            | 3.8.0           |
    | matplotlib-inline          | 0.1.6           |
    | mccabe                     | 0.7.0           |
    | mdit-py-plugins            | 0.3.0           |
    | mdurl                      | 0.1.0           |
    | mistune                    | 2.0.4           |
    | mkl                        | 2023.1.0        |
    | monotonic                  | 1.6             |
    | more-itertools             | 10.1.0          |
    | mpc                        | 1.1.0           |
    | mpfr                       | 4.0.2           |
    | mpmath                     | 1.3.0           |
    | msgpack-python             | 1.0.3           |
    | multidict                  | 6.0.4           |
    | multipledispatch           | 0.6.0           |
    | multiprocess               | 0.70.14         |
    | munkres                    | 1.1.4           |
    | murmurhash                 | 1.0.7           |
    | mypy                       | 1.8.0           |
    | mypy\_extensions           | 1.0.0           |
    | mysql                      | 5.7.24          |
    | nbclient                   | 0.8.0           |
    | nbconvert                  | 7.10.0          |
    | nbformat                   | 5.9.2           |
    | ncurses                    | 6.4             |
    | nest-asyncio               | 1.6.0           |
    | nettle                     | 3.7.3           |
    | networkx                   | 3.1             |
    | ninja                      | 1.10.2          |
    | ninja-base                 | 1.10.2          |
    | nltk                       | 3.8.1           |
    | nodeenv                    | 1.7.0           |
    | notebook                   | 7.0.8           |
    | notebook-shim              | 0.2.3           |
    | nspr                       | 4.35            |
    | nss                        | 3.89.1          |
    | numba                      | 0.59.1          |
    | numexpr                    | 2.8.7           |
    | numpy                      | 1.26.4          |
    | numpy-base                 | 1.26.4          |
    | numpydoc                   | 1.5.0           |
    | oauthlib                   | 3.2.2           |
    | oniguruma                  | 6.9.7.1         |
    | onnxruntime                | 1.17.1          |
    | openai                     | 1.17.0          |
    | opencv                     | 4.6.0           |
    | openh264                   | 2.1.1           |
    | openjpeg                   | 2.4.0           |
    | openpyxl                   | 3.0.10          |
    | openssl                    | 1.1.1w          |
    | opentelemetry-api          | 1.16.0          |
    | opentelemetry-exporter-otl | p-proto-grpc    |
    | opentelemetry-proto        | 1.16.0          |
    | opentelemetry-sdk          | 1.16.0          |
    | opentelemetry-semantic-con | ventions 0.37   |
    | opt\_einsum                | 3.3.0           |
    | orc                        | 1.7.4           |
    | orjson                     | 3.10.0          |
    | overrides                  | 7.4.0           |
    | packaging                  | 23.2            |
    | pandas                     | 2.1.4           |
    | pandocfilters              | 1.5.0           |
    | panel                      | 1.4.1           |
    | param                      | 2.1.0           |
    | parsel                     | 1.8.1           |
    | parso                      | 0.8.3           |
    | partd                      | 1.4.1           |
    | pathspec                   | 0.10.3          |
    | patsy                      | 0.5.3           |
    | pcre2                      | 10.42           |
    | pexpect                    | 4.8.0           |
    | pickleshare                | 0.7.5           |
    | pillow                     | 10.2.0          |
    | pip                        | 23.3.1          |
    | pixman                     | 0.40.0          |
    | platformdirs               | 2.5.2           |
    | plotly                     | 5.19.0          |
    | pluggy                     | 1.0.0           |
    | ply                        | 3.11            |
    | posthog                    | 3.5.0           |
    | pre-commit                 | 3.4.0           |
    | preshed                    | 3.0.6           |
    | prometheus\_client         | 0.14.1          |
    | prompt-toolkit             | 3.0.43          |
    | prompt\_toolkit            | 3.0.43          |
    | protego                    | 0.1.16          |
    | protobuf                   | 3.19.6          |
    | psutil                     | 5.9.0           |
    | ptyprocess                 | 0.7.0           |
    | pulsar-client              | 3.4.0           |
    | pure\_eval                 | 0.2.2           |
    | py-cpuinfo                 | 9.0.0           |
    | py-xgboost                 | 1.7.6           |
    | pyarrow                    | 11.0.0          |
    | pyasn1                     | 0.4.8           |
    | pyasn1-modules             | 0.2.8           |
    | pycodestyle                | 2.10.0          |
    | pycparser                  | 2.21            |
    | pyct                       | 0.5.0           |
    | pycurl                     | 7.45.2          |
    | pydantic                   | 2.5.3           |
    | pydantic-core              | 2.14.6          |
    | pydeck                     | 0.7.1           |
    | pydispatcher               | 2.0.5           |
    | pydocstyle                 | 6.3.0           |
    | pyerfa                     | 2.0.0           |
    | pyflakes                   | 3.0.1           |
    | pygments                   | 2.15.1          |
    | pyjwt                      | 2.4.0           |
    | pylint                     | 2.16.2          |
    | pylint-venv                | 3.0.3           |
    | pyls-spyder                | 0.4.0           |
    | pympler                    | 0.9             |
    | pyodbc                     | 5.0.1           |
    | pyopenssl                  | 23.2.0          |
    | pyparsing                  | 3.0.9           |
    | pypdf                      | 4.2.0           |
    | pypika                     | 0.48.9          |
    | pyqt                       | 5.15.10         |
    | pyqt5-sip                  | 12.13.0         |
    | pyqtwebengine              | 5.15.10         |
    | pysocks                    | 1.7.1           |
    | pytables                   | 3.9.2           |
    | pytest                     | 7.4.0           |
    | python                     | 3.10.13         |
    | python-dateutil            | 2.8.2           |
    | python-dotenv              | 1.0.1           |
    | python-fastjsonschema      | 2.16.2          |
    | python-flatbuffers         | 2               |
    | python-json-logger         | 2.0.7           |
    | python-lmdb                | 1.4.1           |
    | python-lsp-black           | 2.0.0           |
    | python-lsp-jsonrpc         | 1.1.2           |
    | python-lsp-server          | 1.7.2           |
    | python-slugify             | 5.0.2           |
    | python-snappy              | 0.6.1           |
    | python-tzdata              | 2023.3          |
    | python-xxhash              | 2.0.2           |
    | pytoolconfig               | 1.2.6           |
    | pytorch                    | 2.2.0           |
    | pytz                       | 2023.3.post1    |
    | pyviz\_comms               | 3.0.2           |
    | pywavelets                 | 1.5.0           |
    | pyxdg                      | 0.27            |
    | pyyaml                     | 6.0.1           |
    | pyzmq                      | 25.1.2          |
    | qdarkstyle                 | 3.0.2           |
    | qstylizer                  | 0.2.2           |
    | qt-main                    | 5.15.2          |
    | qt-webengine               | 5.15.9          |
    | qtawesome                  | 1.2.2           |
    | qtconsole                  | 5.4.2           |
    | qtpy                       | 2.4.1           |
    | qtwebkit                   | 5.212           |
    | queuelib                   | 1.6.2           |
    | re2                        | 2022.04.01      |
    | readline                   | 8.2             |
    | referencing                | 0.30.2          |
    | regex                      | 2023.10.3       |
    | requests                   | 2.31.0          |
    | requests-file              | 1.5.1           |
    | requests-oauthlib          | 1.3.0           |
    | responses                  | 0.13.3          |
    | rfc3339-validator          | 0.1.4           |
    | rfc3986-validator          | 0.1.1           |
    | rich                       | 13.3.5          |
    | rope                       | 1.12.0          |
    | rpds-py                    | 0.10.6          |
    | rsa                        | 4.7.2           |
    | rtree                      | 1.0.1           |
    | s3fs                       | 2023.10.0       |
    | safetensors                | 0.4.2           |
    | scikit-image               | 0.22.0          |
    | scikit-learn               | 1.3.0           |
    | scipy                      | 1.12.0          |
    | scrapy                     | 2.11.1          |
    | seaborn                    | 0.12.2          |
    | secretstorage              | 3.3.1           |
    | semver                     | 3.0.2           |
    | send2trash                 | 1.8.2           |
    | service\_identity          | 18.1.0          |
    | setuptools                 | 68.2.2          |
    | shellingham                | 1.5.0           |
    | sip                        | 6.7.12          |
    | six                        | 1.16.0          |
    | smart\_open                | 5.2.1           |
    | smmap                      | 4.0.0           |
    | snappy                     | 1.1.10          |
    | sniffio                    | 1.3.0           |
    | snowballstemmer            | 2.2.0           |
    | sortedcontainers           | 2.4.0           |
    | soupsieve                  | 2.5             |
    | spacy                      | 3.7.2           |
    | spacy-legacy               | 3.0.12          |
    | spacy-loggers              | 1.0.4           |
    | sphinx                     | 5.0.2           |
    | sphinxcontrib-applehelp    | 1.0.2           |
    | sphinxcontrib-devhelp      | 1.0.2           |
    | sphinxcontrib-htmlhelp     | 2.0.0           |
    | sphinxcontrib-jsmath       | 1.0.1           |
    | sphinxcontrib-qthelp       | 1.0.3           |
    | sphinxcontrib-serializingh | tml 1.1.5       |
    | spyder                     | 5.4.3           |
    | spyder-kernels             | 2.4.4           |
    | sqlalchemy                 | 2.0.29          |
    | sqlite                     | 3.41.2          |
    | srsly                      | 2.4.8           |
    | stack\_data                | 0.2.0           |
    | starlette                  | 0.37.2          |
    | statsmodels                | 0.14.0          |
    | streamlit                  | 1.16.0          |
    | sympy                      | 1.12            |
    | tabulate                   | 0.9.0           |
    | tbb                        | 2021.8.0        |
    | tblib                      | 1.7.0           |
    | tenacity                   | 8.2.3           |
    | tensorboard                | 2.11.0          |
    | tensorboard-data-server    | 0.6.1           |
    | tensorboard-plugin-wit     | 1.8.1           |
    | tensorflow                 | 2.11.0          |
    | tensorflow-base            | 2.11.0          |
    | tensorflow-estimator       | 2.11.0          |
    | termcolor                  | 2.1.0           |
    | terminado                  | 0.17.1          |
    | text-unidecode             | 1.3             |
    | textdistance               | 4.2.1           |
    | thinc                      | 8.2.2           |
    | threadpoolctl              | 2.2.0           |
    | three-merge                | 0.1.1           |
    | tifffile                   | 2023.4.12       |
    | tiktoken                   | 0.6.0           |
    | tinycss2                   | 1.2.1           |
    | tk                         | 8.6.12          |
    | tldextract                 | 3.2.0           |
    | tokenizers                 | 0.13.2          |
    | toml                       | 0.10.2          |
    | tomli                      | 2.0.1           |
    | tomlkit                    | 0.11.1          |
    | toolz                      | 0.12.0          |
    | tornado                    | 6.3.3           |
    | tqdm                       | 4.65.0          |
    | traitlets                  | 5.7.1           |
    | transformers               | 4.32.1          |
    | twisted                    | 23.10.0         |
    | typer                      | 0.9.0           |
    | typing-extensions          | 4.9.0           |
    | typing-inspect             | 0.9.0           |
    | typing\_extensions         | 4.9.0           |
    | tzdata                     | 2024a           |
    | tzlocal                    | 2.1             |
    | uc-micro-py                | 1.0.1           |
    | ujson                      | 5.4.0           |
    | ukkonen                    | 1.0.1           |
    | unidecode                  | 1.2.0           |
    | unixodbc                   | 2.3.11          |
    | urllib3                    | 2.0.7           |
    | utf8proc                   | 2.6.1           |
    | uvicorn                    | 0.29.0          |
    | uvloop                     | 0.19.0          |
    | validators                 | 0.18.2          |
    | virtualenv                 | 20.17.1         |
    | w3lib                      | 2.1.2           |
    | wasabi                     | 0.9.1           |
    | watchdog                   | 2.1.6           |
    | watchfiles                 | 0.21.0          |
    | wcwidth                    | 0.2.5           |
    | weasel                     | 0.3.4           |
    | webencodings               | 0.5.1           |
    | websocket-client           | 0.58.0          |
    | websockets                 | 12              |
    | werkzeug                   | 2.2.3           |
    | whatthepatch               | 1.0.2           |
    | wheel                      | 0.41.2          |
    | widgetsnbextension         | 4.0.10          |
    | wrapt                      | 1.14.1          |
    | wurlitzer                  | 3.0.2           |
    | x264                       | 1!157.2019121   |
    | xarray                     | 2023.6.0        |
    | xxhash                     | 0.8.0           |
    | xyzservices                | 2022.9.0        |
    | xz                         | 5.4.6           |
    | yaml                       | 0.2.5           |
    | yapf                       | 0.31.0          |
    | yarl                       | 1.9.3           |
    | zeromq                     | 4.3.5           |
    | zfp                        | 1.0.0           |
    | zict                       | 3.0.0           |
    | zipp                       | 3.17.0          |
    | zlib                       | 1.2.13          |
    | zlib-ng                    | 2.0.7           |
    | zope                       | 1               |
    | zope.interface             | 5.4.0           |
    | zstd                       | 1.5.5           |
  </Accordion>
</AccordionGroup>

To see a list of available runtimes, enter the following in a notebook cell then click <Icon icon="play" iconType="solid" /> **Run**:

```sh  theme={null}
!conda info --envs
```

To see a list of packages in your current runtime, enter the following in a notebook cell then click <Icon icon="play" iconType="solid" /> **Run**:

```sh  theme={null}
!conda list
```

## Creating custom runtimes

If you need a specific set of packages that are not included in one of our default runtimes, you can create your own runtime to customize to your needs.

<Note>
  Custom runtimes are stored using your dedicated, persistent Anaconda Notebooks cloud storage. This ensures the custom runtime remains available after your current session ends. Custom runtimes use your personal storage space and can easily get quite large, so *only include the packages you need*.
</Note>

To create a new runtime:

1. Open a terminal from the Launcher, which you can access by selecting the <Icon icon="square-plus" iconType="solid" color="#3874CB" /> blue plus in the top-left corner of the <Icon icon="folder" iconType="solid" /> **File Browser**.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_open_terminal.png?fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=a1af52899940db466142c47ab223a410" data-og-width="1695" width="1695" data-og-height="926" height="926" data-path="images/notebook_open_terminal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_open_terminal.png?w=280&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=2186b9b18c423a67d1ce1030d6e8555c 280w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_open_terminal.png?w=560&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=17e9370ac2dfbd4a5e3d6066394bf458 560w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_open_terminal.png?w=840&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=33145624955da907677fb66bf6426804 840w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_open_terminal.png?w=1100&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=c42f392febce7d8836a6dc0d26b88b55 1100w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_open_terminal.png?w=1650&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=1636250fe1513b0d8b72cb4ba8e7b0d8 1650w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_open_terminal.png?w=2500&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=4f498942b46110286dfc812fb53b4610 2500w" />
   </Frame>

2. Create a new runtime by running the following command:

   ```sh  theme={null}
   # Replace <ENV_NAME> with a new name for your environment/ runtime
   # Replace <PACKAGE> with the name of a package you want to install in your environment
   conda create --name <ENV_NAME> <PACKAGE> ipykernel
   ```

   <Note>
     Adding `ipykernel` creates a Python runtime.
   </Note>

For more information about creating conda environments, see the [official conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Creating a custom runtime from an environment.yml file

<Note>
  This feature is only available for the [local version of Toolbox](/tools/anaconda-notebooks/anaconda-toolbox/local-toolbox).
</Note>

If you have an existing `environment.yml` file, you can create a custom runtime by uploading it to an [Anaconda Toolbox project](/tools/anaconda-notebooks/anaconda-toolbox/using-projects) and installing it directly from there.

#### Uploading an `environment.yml` file

1. Launch Anaconda Notebooks and select the left-side <AnacondaIcon /> **Anaconda Toolbox** icon.

2. Select **Manage Projects**.

3. Select <Icon icon="ellipsis-vertical" iconType="regular" /> actions beside the project where you want to add your `environment.yml` file, then select <Icon icon="upload" iconType="light" /> *Upload*.

4. Select the `environment.yml` file you want to create a custom runtime from. You can use any filename, but the file extension must be `.yml`.

   <Warning>
     The dependencies list must include the `ipykernel` package.

     ***

     The `environment.yml` file must be in valid YAML format.

     ***

     If your `environment.yml` file includes a `name:` key, it will be removed during upload. You'll name your environment during installation.

     See the official [conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually) for more information on creating an `environment.yml` file.
   </Warning>

5. Select **Upload to Project**.

See [Anaconda Projects](/tools/anaconda-notebooks/anaconda-toolbox/using-projects) for more details on creating projects and uploading files.

#### Installing the custom runtime

1. Navigate to the project where you uploaded the `environment.yml` file.

2. Select **Install** beside the `environment.yml` filename.

   <Frame>
     <img src="https://mintcdn.com/anaconda-29683c67/Q1DZa3C8uFqjXt6D/images/notebooks_install_button.png?fit=max&auto=format&n=Q1DZa3C8uFqjXt6D&q=85&s=56917e7e5fad5d109533cf9fb7d8a313" alt="" data-og-width="3460" width="3460" data-og-height="1920" height="1920" data-path="images/notebooks_install_button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/Q1DZa3C8uFqjXt6D/images/notebooks_install_button.png?w=280&fit=max&auto=format&n=Q1DZa3C8uFqjXt6D&q=85&s=9c6ac22660da6f1eb2eda40aab810ea7 280w, https://mintcdn.com/anaconda-29683c67/Q1DZa3C8uFqjXt6D/images/notebooks_install_button.png?w=560&fit=max&auto=format&n=Q1DZa3C8uFqjXt6D&q=85&s=0a14da6c5fc8c389294f66c35d5ac86d 560w, https://mintcdn.com/anaconda-29683c67/Q1DZa3C8uFqjXt6D/images/notebooks_install_button.png?w=840&fit=max&auto=format&n=Q1DZa3C8uFqjXt6D&q=85&s=82af93073772c00bab27e6096aa75b30 840w, https://mintcdn.com/anaconda-29683c67/Q1DZa3C8uFqjXt6D/images/notebooks_install_button.png?w=1100&fit=max&auto=format&n=Q1DZa3C8uFqjXt6D&q=85&s=8ec46c932de22845424afe40595bfccf 1100w, https://mintcdn.com/anaconda-29683c67/Q1DZa3C8uFqjXt6D/images/notebooks_install_button.png?w=1650&fit=max&auto=format&n=Q1DZa3C8uFqjXt6D&q=85&s=64da3e87c6d7c0ad5efadfd3835dca46 1650w, https://mintcdn.com/anaconda-29683c67/Q1DZa3C8uFqjXt6D/images/notebooks_install_button.png?w=2500&fit=max&auto=format&n=Q1DZa3C8uFqjXt6D&q=85&s=17a88b7bc4a25dcd4e6929444094db7f 2500w" />
   </Frame>

3. In the modal that appears, choose a unique name for your environment, then select **Install**.

Once installation is complete, an <Icon icon="pencil" iconType="regular" /> **Edit environment** button appears beside the filename.

Selecting <Icon icon="pencil" iconType="regular" /> **Edit environment** lets you edit your environment with the [Gator environment manager](/tools/anaconda-notebooks/anaconda-toolbox/toolbox-environments#editing-environments-with-gator).

Follow the steps in [Activating a runtime](#activating-runtimes) to activate your custom runtime.

If installation fails, select <Icon icon="copy" iconType="regular" color="red" /> **Copy error logs** beside the filename to troubleshoot. The most common issue is missing the required `ipykernel` package in your dependencies list.

<Note>
  It might take a minute for your custom runtime to be created and available for use. You might need to close and reopen your active notebook or refresh the browser for your new runtime to appear.
</Note>

## Activating runtimes

There are a few locations from which you can activate a runtime:

<Tabs>
  <Tab title="Terminal">
    1. Open a terminal from the Launcher.

    2. Run the following command:

    ```sh  theme={null}
    # Replace <ENV_NAME> with the name of your environment/ runtime
    conda activate <ENV_NAME>
    ```
  </Tab>

  <Tab title="Launcher">
    Select the notebook displaying your custom runtime name.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_launcher-env.png?fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=9083cb734e9e83fe9dac0e40dda8ff6d" alt="" data-og-width="1730" width="1730" data-og-height="926" height="926" data-path="images/notebook_launcher-env.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_launcher-env.png?w=280&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=545df58864877eb820556b8e8c6e2ddb 280w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_launcher-env.png?w=560&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=b0cfa24e34cf7c425dc200117c9c24ee 560w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_launcher-env.png?w=840&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=d64a1d90abde33f72f3391fbb9d102e7 840w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_launcher-env.png?w=1100&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=8da71b19dc7a4cd2c6178515d5591af6 1100w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_launcher-env.png?w=1650&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=13d87b9adf0f53bc35b3a8a864befaef 1650w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_launcher-env.png?w=2500&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=9031b1773d5f1cce6df558349fca5579 2500w" />
    </Frame>
  </Tab>

  <Tab title="Notebook">
    Click the runtime in the top right, then switch to your desired runtime in the Select Runtime modal.

    <Frame>
      <img src="https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_kernel.png?fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=80fae290e5a63016c2b8997a2a4d51ad" alt="" data-og-width="1732" width="1732" data-og-height="413" height="413" data-path="images/notebook_kernel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_kernel.png?w=280&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=b77985710b8d037f630d7b2c8290827e 280w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_kernel.png?w=560&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=45c88f0fea92f8315d20829f3e94815d 560w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_kernel.png?w=840&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=33f4ebc4129c15570555e07c903ba833 840w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_kernel.png?w=1100&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=93cfe252c32bdb513c2f20770ad1fe75 1100w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_kernel.png?w=1650&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=20966b068788f04ba3305cfceb0ed9b0 1650w, https://mintcdn.com/anaconda-29683c67/q5KdI2mr6ZKMYRZp/images/notebook_kernel.png?w=2500&fit=max&auto=format&n=q5KdI2mr6ZKMYRZp&q=85&s=467eb9feceb0873fee549f0fb5fc1b31 2500w" />
    </Frame>
  </Tab>
</Tabs>

## Shutting down runtimes

It is best practice to shut down a runtime when you are finished working in it. To shut down a runtime, click **Kernels** in the top menu, then select the specific runtime you want to shut down or **Shut Down All**.

## Managing packages in a runtime

### Installing additional packages

Even after you've created a runtime, you can continue to add packages as needed. To add a package to a custom runtime:

1. Open a terminal from the Launcher.

2. Activate the runtime environment by running the following command:

   ```sh  theme={null}
   # Replace <ENV_NAME> with the name of the runtime environment
   conda activate <ENV_NAME>
   ```

3. Install the packages you want to add to the environment:

   ```sh  theme={null}
   # Replace <PACKAGE> with the name of the package you want to install
   conda install <PACKAGE>
   ```

Verify the package was installed by [activating the runtime](#activating-runtimes) and running the following command in a notebook cell:

```sh  theme={null}
!conda list
```

### Updating packages

To update packages in your runtime:

1. Open a terminal from the Launcher.

2. Activate the environment by running the following command:

   ```sh  theme={null}
   # Replace <ENV_NAME> with the name of the environment
   conda activate <ENV_NAME>
   ```

3. To update the package:

   ```sh  theme={null}
   # Replace <PACKAGE> with the name of the package you want to update
   conda update <PACKAGE>
   ```

### Removing packages

To remove packages in your runtime:

1. Open a terminal from the Launcher.

2. Activate the environment by running the following command:

   ```sh  theme={null}
   # Replace <ENV_NAME> with the name of the environment
   conda activate <ENV_NAME>
   ```

3. To remove the package:

   ```sh  theme={null}
   # Replace <PACKAGE> with the name of the package you want to update
   conda remove <PACKAGE>
   ```

## Removing custom runtimes

To remove a custom runtime:

1. Open a terminal from the Launcher.

2. Run the following command to remove the custom runtime:

```sh  theme={null}
# Replace <ENV_NAME> with a new name for your environment/ runtime
conda env remove --name <ENV_NAME>
```

The custom runtime no longer appears in the kernel selector or Launcher.

## Troubleshooting

### "Missing ipykernel dependency" error

A `missing ipykernel dependency` error is caused by an environment dependency list not including the required `ipykernel` package. To resolve this issue, add the `ipykernel` package to your environment's dependency list. For example:

```yml highlight {7} theme={null}
channels:
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - ipykernel
```

￼