from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
#manager.pyからデータ構造をimport
from manager.models import TB_Worker,TB_Skill,TB_VsSkill
from manager.forms import SkillSerchForm,SkillRegForm,WorkerRegForm,WorkerSkillRegForm
from django.db.models import Q

# Create your views here.
#ここでviewを作る
class WorkerListView(TemplateView):
 template_name = "worker_list.html"
 def get(self, request, *args, **kwargs):
    context = super(WorkerListView, self).get_context_data(**kwargs)

    #検索フォームに関する処理
    form = SkillSerchForm(self.request.GET or None)
    context['form'] = form
    
    if form.is_valid():
       #フォームから入力されたスキル名を取り出す
       skill_name = form.cleaned_data.get("skill_name")
       context['skill_name'] = skill_name

       #スキル名に対応するスキルIDを取り出す(クエリの取り出しはできる)
       #スキル名の検索は完全一致(exact)で行う
       skill_code_Q = TB_Skill.objects.filter(Q(name__exact=skill_name))
      #一致するスキル名が存在しない時
       if skill_code_Q.first() == None:
         context['message'] = "スキルテーブルに一致するスキルが存在しません"
         return render(self.request, self.template_name, context)
       else:
         #クエリからスキルコードの抜き出し
         skill_code = skill_code_Q.get().skill_code
         context['skill_code'] = skill_code
         #htmlにはskill_codeに対応したTB_VsSkillのクエリセットを求める
         s_worker = TB_VsSkill.objects.filter(skill_code__skill_code=skill_code)
         context['select_worker'] = s_worker
         return render(self.request, self.template_name, context)

    else:
       return render(self.request, self.template_name, context)

#スキル登録画面
class SkillRegisterView(TemplateView):
  template_name = "skill_reg.html"

  def get(self, request, *args, **kwargs):
    context = super(SkillRegisterView, self).get_context_data(**kwargs)
    #登録フォーム
    form = SkillRegForm(self.request.GET or None)
    context['form'] = form

    if (form.is_valid()):
      context['message'] = "スキル登録が完了しました"
      skill_code = form.cleaned_data.get("code")
      skill_name = form.cleaned_data.get("name")
      context['skill_code'] = skill_code
      context['skill_name'] = skill_name
      TB_Skill.objects.create(skill_code=skill_code, name =skill_name)
      #DBに登録
      return render(self.request, self.template_name, context)
    else:
      context['message'] = "有効なスキルコードを入力してください"
      return render(self.request, self.template_name, context)

#社員登録画面
class WorkerRegisterView(TemplateView):
  template_name = "worker_reg.html"

  def get(self, request, *args, **kwargs):
    context = super(WorkerRegisterView, self).get_context_data(**kwargs)
    #登録フォーム
    form = WorkerRegForm(self.request.GET or None)
    context['form'] = form

    if (form.is_valid()):
      context['message'] = "スキル登録が完了しました"
      worker_code = form.cleaned_data.get("code")
      worker_name = form.cleaned_data.get("name")
      worker_dep = form.cleaned_data.get("dep")
      worker_mail = form.cleaned_data.get("mail")
      context['worker_code'] = worker_code
      context['worker_name'] = worker_name
      context['worker_dep'] = worker_dep
      context['worker_mail'] = worker_mail
      TB_Worker.objects.create(worker_code=worker_code, name=worker_name,dep=worker_dep,mail=worker_mail)
      #DBに登録
      return render(self.request, self.template_name, context)

    else:
      context['message'] = "有効な社員コードを入力してください"
      return render(self.request, self.template_name, context)

#社員スキル保有スキル登録画面
#スキルコードから、スキル名を逆引き⇨vsTableに登録する
class WorkerSkillRegisterView(TemplateView):
  template_name = "worker_skill_reg.html"
  def get(self, request, *args, **kwargs):
    context = super(WorkerSkillRegisterView, self).get_context_data(**kwargs)

    form = WorkerSkillRegForm(self.request.GET or None)
    context['form'] = form

    if (form.is_valid()):
      #formからデータを取得
      worker_code = form.cleaned_data.get("worker_code")
      skill_name = form.cleaned_data.get("skill_name")
      #入力されたスキルをDBのTB_Skillから検索し、クエリを取得
      TB_Skill_Q = TB_Skill.objects.filter(Q(name__exact=skill_name))
      #スキル表のスキル名が有る無し?
      if TB_Skill_Q.first() == None:
        context['message'] = "入力されたスキルは存在しません"
        return render(self.request, self.template_name, context)
      else:
        #社員が存在するかを調べていく
        TB_Worker_Q = TB_Worker.objects.filter(Q(worker_code__exact=worker_code))
        if TB_Worker_Q.first() == None:
          context['message'] = "入力された社員は存在しません"
          return render(self.request, self.template_name, context)
        else:
          #クエリからスキルコードを抜き出す
          skill_code = TB_Skill_Q.get().skill_code
          #worker_codeとskill_codeをTB_VsSkillに登録していく
          w = get_object_or_404(TB_Worker, worker_code=worker_code)
          s=get_object_or_404(TB_Skill, skill_code=skill_code)
          TB_VsSkill.objects.create(worker_code=w, skill_code=s)
          context['message'] = "スキル登録完了しました"
          return render(self.request, self.template_name, context)
    else:
      context['message'] = "社員コードとスキル名を入力してください"
      return render(self.request, self.template_name, context)

