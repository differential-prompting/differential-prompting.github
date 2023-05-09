---
icon: fas fa-tag
order: 1
---

## Downloads
[**Piecer**](https://github.com/Piecer-plc/piecer-plc)
## Run Piecer
- Step 1

Download the source code and install the requirements.
```python
pip install requirements.txt
```
- Step 2


Create the database table and add the pipeline info.
- Step 3

Extract direct dependency of the pipeline.

```python
# dependency_analysis.project_dependency_analysis.project_dependency_analysis.py
if __name__ == "__main__":
    # pipeline file path
    file_path = ""
    # pipeline id
    pipeline_id = ""
    analysis_pipeline_direct_dependencies(file_path,pipeline_id)
```
- Step 4

Extract indirect dependency of the pipeline.
```python
# dependency_analysis.package_requirement_analysis.package_requirement_analysis.py
if __name__ == "__main__":
    # library name
    pkg_name = ""
    # library version
    pkg_version = ""
    # path of library(local path)
    pkg_path = ""
    analysis_package_dependency(pkg_name, pkg_version, pkg_path)
```
- Step 5

Build installable versions pool.
```python
# build_envirement.build_dependency_pool.py
if __name__ == "__main__":
    
    from model.pipeline_dependency import PipelineDeps
    from model.dependency_pool import DepsPool
    # pipeline_id 
    # python_version 
    build_pool = DepPoolBuild(pipeline_id=32252, python_version='3.7.10')
    build_pool.create_pipeline_deps_pool_group()
```
- Step 6

Generate library version combinations variants.
```python
# build_envirement.build_install_info.py
if __name__ == "__main__":
    pipeline_id = 1
    # os_name  windows : "win_amd64" ， linux: os name
    # stages = []  the libraries in this stage will considered. 
	  # non_fixed_deps= []  libraries not considered
	  # fixed_deps = []     libraries  considered
    cre = CreateRunInfo(pipeline_id=pipeline_id, stages=[], py_version="3.7.10", os_name="win_amd64",experiment_No=1,non_fixed_deps=None, fixed_deps=None)
    cre.create()
```
- Step 7

Run.
```python
# run_experiment.run_experiments.py
if __name__ == "__main__":
    root = ""
    venv_root = ""
    package_root= ""
    output_folder = ""
    computer_num = ""
    python_version = ""
    input_root = ""
    concerned_stages = []
    experiment_No = ""
    support_os = ""
    run_ex = RunExperiment(root,venv_root,package_root,output_folder,computer_num,python_version,input_root,concerned_stages,experiment_No,support_os)
    pipeline_id = 1
    run_ex.run_pipeline(pipeline_id)
```
<div id="d-help-win" class="d-help-win" >
    <div id="win-title">Help
        <span id="d-help-colse" clss="close_2" class="close_2">
            × 
        </span>
    </div>
    <div id="win-content">
        <!-- 我们提供了xxx数据集。
        1.
        2.
        3.
        4.
        查看详细复现结果：
        动图！ -->
        <img src="/assets/images/Pipeline-Bug.gif">
    </div>
</div>
 <div id="d-help-win" class="d-help-win" style="display: none;">
      <div id="win-title">Help
          <span id="d-help-colse" clss="close_2" class="close_2">
              × 
          </span>
      </div>
      <div id="win-content">
          <blockquote class="prompt-tip"><div><p> We provide a list of PLC issues captured by us in real-world pipelines and popular ML libraries.</p></div></blockquote>
          <div>
              <ol>
                  <li>Go to <strong><font color="#FF0000">Empirical Findings</font></strong> page</li>
                  <li>Select a bug and click on <strong><font color="#FF0000">reproduce result link</font></strong>.</li>
                  <li>You can find the reproduction results of each version and the related reproduction code.</li></ol>
          </div>
          <!-- 我们提供了xxx数据集。
          1.
          2.
          3.
          4.
          查看详细复现结果：
          动图！ -->
          <img src="/assets/images/Pipeline-Bug.gif" alt="avatar">
      </div>
  </div>
